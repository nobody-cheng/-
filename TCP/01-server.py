import socket
# from socket import *
#
# # 创建
# sock = socket(AF_INET, SOCK_STREAM)
#
# #  绑定
# sock.bind(('', 10086))
#
# #  设置监听
# sock.listen(250)
#
# #  接收连接
# newsock, addr = sock.accept()
#
# #  接收数据
# data = newsock.recv(1024)
# print(data)
# print(addr)
#
# #  发送（回应）数据
# newsock.send('hello from server'.encode())
#
# #  关闭socket
# newsock.close()
# sock.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('', 10086))
server_socket.listen(220)
client_socket, client_addr = server_socket.accept()
recv_data = client_socket.recv(1024)
print('接收到的信息是：%s' % recv_data.decode())
print('地址:',client_addr)

client_socket.send('hi from server'.encode())
server_socket.close()






