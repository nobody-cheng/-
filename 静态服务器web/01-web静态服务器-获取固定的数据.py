import socket

def main():
    """整体的流程控制"""
    # 创建tcp的套接字
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定信息
    server_socket.bind(("",8888))
    # 监听变为被动的套接字
    server_socket.listen(250)
    while True:
        # accpet
        new_socket, new_add = server_socket.accept()
        # 接受数据
        recv_data = new_socket.recv(2048)

        # 返回一个固定的数据
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "\r\n"
        response_body = "heihei hello world"
        response = response_header + response_body

        new_socket.send(response.encode())
        new_socket.close()

        # 正则表达式 解析发送过来的请求

        # 找到对应的文件 打开文件读取数据 返回给客户端

if __name__ == '__main__':
    main()