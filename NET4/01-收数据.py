import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('', 10086))

print(sock.recvfrom(1024))
