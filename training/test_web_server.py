import socket
import re
import sys
import gevent
from gevent import monkey

# 打补丁
monkey.patch_all()
g_dynamic_root = './dynamic'
client_sockets = []


class WSGIServer(object):
    def __init__(self, port, root_path, app):
        # 创建tcp套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.server_socket)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定信息
        self.server_socket.bind(('', port))
        # 监听变为被动套接字
        self.server_socket.listen(250)
        self.documents_root = root_path
        self.app = app
        self.headers = []

    def run_forever(self):
        while True:
            # accept
            new_socket, new_addr = self.server_socket.accept()
            gevent.spawn(self.handle_with_request, new_socket)

    def handle_with_request(self, new_socket):
        # 多次数据处理
        while True:
            # 接收数据
            recv_data = new_socket.recv(2048)
            # 判断是否有数据，解码
            if not recv_data:
                new_socket.close()
                return
            request = recv_data.decode()
            print('~~~~~~~~request~~~~~~~~~~~', request)

            request_lines = request.splitlines()
            for i, line in enumerate(request_lines):
                print(i, line)
                # 正则表达式 解析发送过来的请求
                #  GET / HTTP/1.1
                # GET /index.html HTTP/1.1
                # POST /xxx.html
                # GET /home/show_goods.html
                # GET /home/logo.png
                # [^ ]
            ret = re.match(r'([^/]*)([^ ]*)', request_lines[0])
            file_path = ret.group(2)
            if file_path == '/':
                file_path = '/index.html'
            print('~~~~~~~file_path~~~~~~~~~', file_path)
            # 处理动态资源
            if not file_path.endswith('.html'):
                # css png js
                # 静态数据
                # 找到对应的文件 打开文件读取数据 返回给客户端
                try:
                    f = open(self.documents_root + file_path, 'rb')
                except Exception as result:
                    print('请求网页失败：', result)
                    # 404
                    response_body = 'SORRY,没有你请求的文件'
                    response_header = 'HTTP/1.1 404 Not Fount\r\n'
                    response_header += 'Content-Type: text/html; charset=utf-8\r\n'
                    response_header += 'Content-Length: %d\r\n' % len(response_body.encode())
                    response_header += '\r\n'
                    response = response_header + response_body
                    new_socket.send(response.encode())
                else:
                    content = f.read()
                    response_body = content
                    response_header = 'HTTP/1.1 200 OK\r\n'
                    response_header += 'Content-Length: %d\r\n' % len(response_body)
                    response_header += '\r\n'

                    new_socket.send(response_header.encode())
                    new_socket.send(response_body)
            else:
                # .html结尾的动态数据
                # 准备参数 file_path
                envi = {'PATH_INFO': file_path}
                response_body = self.app(envi, self.start_response)
                if response_body:
                    response_header = 'HTTP/1.1 %s\r\n' % self.headers[0]
                    for item in self.headers[1]:
                        # item是一个元祖(content-type, text/html)
                        response_header += '%s: %s\r\n' % (item[0], item[1])
                    response_header += 'Content-Length: %d\r\n' % len(response_body.encode())
                    response_header += '\r\n'
                    response = response_header + response_body
                    new_socket.send(response.encode())

    def start_response(self, status, response_headers):
        # 获取到头信息
        self.headers = [status, response_headers]


def main():
    if len(sys.argv) == 3:
        port_str = sys.argv[1]
        if port_str.isdigit():
            port = int(port_str)
        else:
            print('请输入正确的端口号')
            return
        # test_my_web:app
        print(sys.path)
        sys.path.append(g_dynamic_root)
        params = sys.argv[2]
        ret = re.match(r'(.*):(.*)', params)
        module_name = ret.group(1)
        func_name = ret.group(2)
        my_web_module = __import__(module_name)
        app = getattr(my_web_module, func_name)

    else:
        print('请以 python3 xxx.py 8888 my_web:app 方式运行服务器')
        return
    # 实例化服务对象
    wsgi_server = WSGIServer(port, './static', app)
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()

