import socket
import multiprocessing
import re
import sys


class WSGIServer(object):
    def __init__(self, port, root_path):
        # 创建套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 重复使用端口
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定端口
        self.server_socket.bind(('', port))
        # 进行监听套接字变为被动套接字
        self.server_socket.listen(250)
        self.documents_root = root_path

    def run_forever(self):
        while True:
            # 不断接收新的客户端
            new_socket, new_addr = self.server_socket.accept()
            print('~~~~~新的客户端~~~~~', new_addr)
            # 创建多进程
            new_process = multiprocessing.Process(target=self.handle_with_request, args=(new_socket,))
            # 启动线程
            new_process.start()
            new_socket.close()

    def handle_with_request(self, new_socket):
        # 接收数据
        recv_data = new_socket.recv(1024)
        # 进行判断是否有数据
        if not recv_data:
            return
        # 有数据进行解码
        request = recv_data.decode()
        """
                GET / images / trolltech - logo.png
                HTTP / 1.1
                Host: localhost:8888
                Connection: keep - alive
                Accept: image / webp, image / *, * / *;q = 0.8
                User - Agent: Mozilla / 5.0(X11;
                Linux
                x86_64) AppleWebKit / 537.36(KHTML, like
                Gecko) Chrome / 50.0
                .2661
                .102
                Safari / 537.36
                Referer: http: // localhost: 8888 /
                Accept - Encoding: gzip, deflate, sdch
                Accept - Language: zh - CN, zh;
                q = 0.8
        """
        request_line = request.splitlines()
        for i, item in enumerate(request_line):
            print(i, item)
        """
                0 GET /favicon.ico HTTP/1.1
                1 Host: localhost:8888
                2 Connection: keep-alive
                3 Pragma: no-cache
                4 Cache-Control: no-cache
                5 User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
                6 Accept: */*
                7 Referer: http://localhost:8888/
                8 Accept-Encoding: gzip, deflate, sdch
                9 Accept-Language: zh-CN,zh;q=0.8
                10

        """
        ret = re.match(r'([^/]*)([^ ]*)', request_line[0])
        file_path = ret.group(2)
        if file_path == '/':
            file_path = '/index.html'
        print('~~~~~file_path~~~~~~', file_path)

        try:
            f = open(self.documents_root + file_path, 'rb')
        except Exception as result:
            # 返回失败信息到客户端页面
            response_header = 'HTTP/1.1 404 Not Found\r\n'
            response_header += 'Content-Type: text/html; charset=utf-8\r\n'
            response_header += '\r\n'
            response_body = '对不起，请求错误页面'
            response = response_header + response_body
            new_socket.send(response.encode())

        else:
            content = f.read()
            f.close()
            response_header = 'HTTP/1.1 200 OK\r\n'
            response_header += '\r\n'
            response_body = content
            new_socket.send(response_header.encode())
            new_socket.send(response_body)

        finally:
            new_socket.close()


def main():
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
    wsgi_server = WSGIServer(port, './html')
    wsgi_server.run_forever()

if __name__ == '__main__':
    main()
