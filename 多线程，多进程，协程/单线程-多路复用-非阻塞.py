import socket
import threading
import re
import sys
import select
import time


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
        # 设置非阻塞状态
        self.server_socket.setblocking(False)
        # 添加客户端列表
        self.client_sockets = []

    def run_forever(self):
        while True:
            # 判断是否有新的客户端，有新客户端判断是否有数据
            try:
                # 不断接收新的客户端
                new_socket, new_addr = self.server_socket.accept()
            except Exception as result:
                print('没有新的客户端连接', result)
            else:
                # 有新的客户端,再次设置为非阻塞状态，添加到列表中保存
                new_socket.setblocking(False)
                self.client_sockets.append(new_socket)
            time.sleep(0.8)
            # 遍历客户端列表
            for client_socket in self.client_sockets:
                # 判断是否有新的数据
                try:
                    recv_data = client_socket.recv(1024)
                except Exception as result:
                    print('没有新的数据', result)
                else:
                    # 收到新的数据
                    if recv_data:
                        self.handle_with_request(recv_data, client_socket)
                    else:
                        # 数据长度为0
                        client_socket.close()
                        self.client_sockets.remove(client_socket)

    def handle_with_request(self, recv_data, new_socket):
        # 接收数据

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
