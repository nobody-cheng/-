#  客户端
from socket import *

sock = socket(AF_INET, SOCK_DGRAM)

sock.sendto('你好,我是发送数据'.encode(), ('127.0.0.1', 10086))

data, addr = sock.recvfrom(1024)

data = data.decode()
print(data, addr)
