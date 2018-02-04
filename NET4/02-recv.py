#  服务器
from socket import *

sock = socket(AF_INET, SOCK_DGRAM)

sock.bind(('', 10086))

data, addr = sock.recvfrom(10099)

data = data.decode()
print(data, addr)

sock.sendto('你好,我是接收数据'.encode(), addr)
