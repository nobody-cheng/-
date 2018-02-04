# from socket import *
# # 创建socket
# sock =socket(AF_INET, SOCK_STREAM)
#
# #  连接服务器
# sock.connect(('127.0.0.1', 10086))
#
# #  发送数据
# sock.send('hello from client'.encode())
#
# # 接收数据
# data = sock.recv(1024)
#
# print(data)
#
# sock.close()

import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.1.1', 10086))
client_socket.send('hello from client'.encode())

data= client_socket.recv(1024)
print('data:%s' %data.decode())