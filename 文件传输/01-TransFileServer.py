from socket import *
from threading import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('', 10086))
server.listen(250)


# 服务客户端的线程
def client(sock, data):

    # 读取文件名长度
    readLen = 0
    data = b''
    while True:
        readData = sock.recv(8 - readLen)
        data += readData
        readLen += len(readData)
        if readLen == 8:
            break

    totallen = int(data.decode())
    print('filename len is', totallen)

    # 读取文件名
    readLen = 0
    data = b''
    while True:
        readData = sock.recv(totallen - readLen)
        data += readData
        readLen += len(readData)
        if totallen == len(readLen):
            break
    filename = data.decode()
    print('filename is ', filename)

    oFile = open(filename, 'wb')

    # 读取文件内容长度
    readLen = 0
    data = b''
    while True:
        readData = sock.recv(8 - readLen)
        data += readData
        readLen += len(readData)
        if readLen == len(readData):
            break
    totallen = int(data.decode())
    print('file len is', totallen)

    # 读取文件内容
    readLen = 0
    data = b''
    while True:
        readData = sock.recv(1024)
        oFile.write(readData)
        readLen += len(readData)
        if readLen == totallen:
            break
    oFile.close()

# 不停尝试接收客户端连接
while True:
    sock, addr = server.accept()
    thread = Thread(target=client, args=(sock, addr))
    thread.start()

