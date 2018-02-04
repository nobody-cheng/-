from socket import *

sock = socket(AF_INET, SOCK_DGRAM)

sock.bind(('', 10086))

data, addr = sock.recvfrom(1024)

print(data, addr)
