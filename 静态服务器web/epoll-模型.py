import socket
import select


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR ,1)
    server_socket.bind(('', 8888))
    server_socket.listen(250)

    # 创建一个epoll对象
    epoll = select.epoll()
    print(server_socket.fileno())
    print(select.EPOLLIN|select.EPOLLET)

    epoll.register(server_socket.fileno(), select.EPOLLIN | select.EPOLLET)

if __name__ == '__main__':
    main()