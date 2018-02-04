import socket

port = 10086  # 服务器端口号
# 创建服务器套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
server_socket.bind(('', port))
# 进行监听，变为被动套接字
server_socket.listen(220)
# 接收客户端发送过来的消息及地址信息
client_socket, client_addr = server_socket.accept()
# 对接收消息进行解码
recv_data = client_socket.decode()
print(recv_data)

msg = recv_data
# 把接收到的消息返回客户端
client_socket.send(msg.encode())
# 关闭套接字
server_socket.close()