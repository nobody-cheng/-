from socket import *
import time


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', 8888))
    server_socket.listen(250)
    server_socket.setblocking(False)

    client_sockets = []

    while True:
        try:
            # 不断检测有无客户端
            new_socket, new_addr = server_socket.accept()
        except Exception as result:
            print('没有新的客户段连接',result)
        else:
            # 新的客户端连接设置非阻塞,添加到列表中
            new_socket.setblocking(False)
            client_sockets.append(new_socket)
        # 遍历列表，检测所有客户端有无数据发送过来
        time.sleep(0.8)
        for client_socket in client_sockets:
            # 检测是否有新数据
            try:
                recv_data = client_socket.recv(1024)
            except Exception as result:
                print('没有客户端发送数据过来', result)
            else:
                # 接收到数据
                if recv_data:
                    response_body = 'hello python'
                    response_header = 'HTTP/1.1 200 OK\r\n'
                    response_header += 'Content-Length: %d\r\n' % len(response_body.encode())
                    response_header += '\r\n'

                    response = response_header + response_body
                    client_socket.send(response.encode())
                else:
                    # 没有数据，关闭，删除
                    client_socket.close()
                    client_sockets.remove(client_socket)


if __name__ == '__main__':
    main()


