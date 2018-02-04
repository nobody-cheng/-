import socket
import re
import sys
import time
import select

class WSGIServer(object):
    def __init__(self, port, root_path):
        # 创建tcp的套接字
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定信息
        self.server_socket.bind(("", port))
        # 监听变为被动的套接字
        self.server_socket.listen(250)
        # 设置为非阻塞
        self.server_socket.setblocking(False)
        self.documents_root = root_path
        self.client_sockets = []


    def run_forever(self):

        while True:

            try:
                # accpet
                new_socket, new_add = self.server_socket.accept()
            except Exception as ret:
                print("没有新的客户端连接过来",ret)
            else:
                # 新客户端连接了
                new_socket.setblocking(False)
                self.client_sockets.append(new_socket)
            time.sleep(1)
            # 遍历列表  轮询
            for client_socket in self.client_sockets:
                try:
                    recv_data = client_socket.recv(2048)
                except Exception as ret:
                    print("没有收到数据",ret)
                else:
                    # 收到数据
                    if recv_data:
                        self.handle_with_request(recv_data, client_socket)
                    else:
                        # 数据长度为0
                        client_socket.close()
                        self.client_sockets.remove(client_socket)



    def handle_with_request(self, recv_data, new_socket):
        # 接受数据

        request = recv_data.decode()
        # print(request)
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
        ret = re.match(r"([^/]*)([^ ]*)", request_lines[0])
        file_path = ret.group(2)
        if file_path == "/":
            file_path = "/index.html"
        print("++++++++++++++++文件的路径:", file_path)
        # 找到对应的文件 打开文件读取数据 返回给客户端
        try:
            f = open(self.documents_root + file_path, "rb")
        except Exception as ret:
            print("打开文件失败:", ret)
            # 404
            response_body = "sorry,没有你要的文件"

            response_header = "HTTP/1.1 404 Not Found\r\n"
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length: %d\r\n" % len(response_body.encode())
            response_header += "\r\n"

            response = response_header + response_body
            new_socket.send(response.encode())
            # close
            # new_socket.close()

        else:
            content = f.read()
            response_body = content

            response_header = "HTTP/1.1 200 OK\r\n"
            response_header += "Content-Type: text/html; charset=utf-8\r\n"
            response_header += "Content-Length: %d\r\n" % len(response_body)
            response_header += "\r\n"

            new_socket.send(response_header.encode())
            new_socket.send(response_body)

def main():
    """整体的流程控制"""
    if len(sys.argv) == 2:
        port_str = sys.argv[1]
        if port_str.isdigit():
            port = int(port_str)
        else:
            print("请输入正确的端口号")
            return
    else:
        print("请以 python3 xxx.py 8888 方式运行服务器")
        return

    # 实例化服务对象
    wsgi_server = WSGIServer(port, "./html")
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()