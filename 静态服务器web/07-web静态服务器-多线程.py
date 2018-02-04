import socket
import re
import sys
import threading


class WSGIServer(object):
    def __init__(self, port, root_path):
        # 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 重复使用端口
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定端口
        self.server_socket.bind(('', port))
        #  设置监听,变为被动的套接字
        self.server_socket.listen(250)
        self.documents_root = root_path

    def run_forever(self):
        while True:
            # 接受连接accept
            new_socket, new_addr = self.server_socket.accept()
            # 创建进程
            new_thread = threading.Thread(target=self.handle_with_request, args=(new_socket,))
            new_thread.start()


    def handle_with_request(self, new_socket):
        # 接收数据
        recv_data = new_socket.recv(1024)
        # 判断是否有数据，然后进行解码
        if not recv_data:
            return
        request = recv_data.decode()
        # print(request)
        request_lines = request.splitlines()
        print(request_lines)
        for i, line in enumerate(request_lines):
            print(i, line)
        # 正则表达式 解析发送过来的请求

        ret = re.match(r'([^/]*)([^ ]*)', request_lines[0])
        file_path = ret.group(2)

        if file_path == '/':
            file_path = '/index.html'
        print('================文件的路径', file_path)

        # 找到对应的文件，打开文件读取数据，返回客户端
        try:
            f = open(self.documents_root + file_path, 'rb')
        except Exception as ret:
            print('打开文件失败', ret)
            response_header = 'HTTP/1.1 404 Not Found\r\n'
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += '\r\n'
            response_body = 'sorry,请求页面失败'
            response = response_header + response_body
            new_socket.send(response.encode())

        else:
            content = f.read()

            # 返回一个固定的数据
            response_header = 'HTTP/1.1 200 OK\r\n'
            response_header += '\r\n'
            response_body = content
            # response = response_header + response_body,字符串和二进制无法运算

            new_socket.send(response_header.encode())
            new_socket.send(response_body)
            # new_socket.close()
        finally:
            new_socket.close()


def main():
    """整体的流程控制"""
    if len(sys.argv) == 2:
        port_str = sys.argv[1]
        if port_str.isdigit():
            port = int(port_str)
        else:
            print('请输入正确的端口号')
            return
    else:
        print('请以 python3 xxx.py 8888方式运行服务器')
        return
    # 实例化服务对象
    wsgi_server = WSGIServer(port, './html')
    wsgi_server.run_forever()

if __name__ == '__main__':
    main()