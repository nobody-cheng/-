from socket import *
import time


def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('', 7788))
    server_socket.listen(220)
    # 新建列表保存新的套接字
    client_sockets = []

    # 设置非阻塞
    server_socket.setblocking(False)
    while True:
        try:
            # 不断检测是否有新的客户端
            new_socket, new_addr = server_socket.accept()
        except Exception as result:
            print('没有新的客户端连接', result)
        else:
            # 有新的客户端连接， 设置新的客户端为非阻塞
            server_socket.setblocking(False)
            client_sockets.append(new_socket)
        # 遍历client_sockets ,检测有无数据发送过来
        time.sleep(1.2)
        print(client_sockets)
        for client_socket in client_sockets:
            # 尝试接收新数据
            try:
                recv_data = client_socket.recv(1024)
            except Exception as result:
                print('没有接收到客户端发送的新数据', result)
            else:
                # 接收到数据
                if recv_data:
                    print('++++++++++++收到数据+++++++')
                    response_body = 'hello python'
                    response_header = 'HTTP/1.1 200 OK'
                    response_header += 'Content-Length: %d\r\n' % len(response_body.encode())
                    response_header += '\r\n'

                    response = response_header + response_body
                    client_socket.send(response.encode())

                else:
                    # 没有收到数据，进行关闭和删除
                    client_socket.close()
                    client_sockets.remove(client_socket)

if __name__ == '__main__':
    main()