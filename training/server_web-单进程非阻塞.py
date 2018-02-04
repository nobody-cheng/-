import socket
import sys
import re
import time

# g_documents_root = './html'


class WSGIServer(object):
    def __init__(self, port, root_path):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 不断重复利用端口
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.setblocking(False)
        self.server_socket.bind(('', port))
        self.server_socket.listen(250)
        self.documents_root = root_path
        self.client_sockets = []

    def run_forever(self):
        while True:
            #判断有无新的客户端
            # 不断接收新的客户端
            try:
                new_socket, new_addr = self.server_socket.accept()
            except Exception as result:
                print('无新的客户端连接', result)
            else:
                # 有新的客户端连接，添加到列表,设置阻塞
                new_socket.setblocking(False)
                self.client_sockets.append(new_socket)
                # 对列表进行遍历所有新的客户端
            time.sleep(0.8)
            # 遍历列表
            for client_socket in self.client_sockets:
                try:
                    recv_data = client_socket.recv(2048)
                except Exception as result:
                    print('没有收到新的数据', result)
                else:
                    # 收到新数据
                    if recv_data:
                        self.handle_with_request(recv_data, client_socket)
                    else:
                        # 数据长度为0
                        client_socket.close()
                        self.client_sockets.remove(client_socket)

    def handle_with_request(self, recv_data, new_socket):
        request = recv_data.decode()

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

        try:
            f = open(self.documents_root + file_path, 'rb')
        except Exception as ret:
            print('打开文件失败', ret)
            response_body = 'sorry,请求页面失败'
            response_header = 'HTTP/1.1 404 Not Found\r\n'
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += 'content-length: %d\r\n' % len(response_body)
            response_header += '\r\n'
            response = response_header + response_body
            new_socket.send(response.encode())

        else:
            content = f.read()
            response_body = content
            f.close()
            # 返回一个固定的数据
            response_header = 'HTTP/1.1 200 OK\r\n'
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length: %d\r\n" % len(response_body)
            response_header += '\r\n'
            # response = response_header + response_body,字符串和二进制无法运算

            new_socket.send(response_header.encode())
            new_socket.send(response_body)
        # finally:
        #     new_socket.close()


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
    wsgi_server = WSGIServer(port, './html')
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()



