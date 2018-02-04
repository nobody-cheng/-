"""读取文件名长度，读文件名，读文件内容长度，读文件内容"""
from socket import *
from threading import *
import os


# def writeData(sock, data):
#     writeLen = 0
#
#     while True:
#         ret = sock.send(data[writeLen:])
#         writeLen += ret
#         if writeLen == len(data):
#             break


def sendFileThread(filepath, ip):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((ip, 10089))

    filename = os.path.basename(filepath)  # 获得文件名

    # 先发送文件名长度
    filenameData = filename.encode()  # 编码
    filenameLen = len(filenameData)  # 编码后的长度
    filenamelenStr = '%08d' % filenameLen  # 转换成8字节的长度
    filenamelenData = filenamelenStr.encode()  # 转换8字节的长度后再编码得到文件名长度
    # 发送文件名长度
    sock.send(filenamelenData)
    # 发送文件名
    sock.send(filenameData)

    #  发送文件内容的长度
    filename = filepath  # 文件路径
    filelen = os.path.getsize(filename)  # 文件内容长度
    filelenStr = '%08d' % filelen  # 8字节的长度
    filelenStrData = filelenStr.encode()  # 编码后的长度
    # 发送文件内容长度
    sock.send(filelenStrData)

    iFile = open(filename, 'rb')
    while True:
        data = iFile.read(1024)
        if not data:
            break
        # sock.send(data) # 一次性全发送会造成丢失
        writeByData(sock, data)

#  写入内容的函数
def writeByData(sock, data):
    writelen = 0
    while True:
        ret = sock.send(data[writelen:])
        writelen += ret
        if writelen == len(data):
            break

#  要求读取多长的数据
def readByLen(sock, totalLen):
    readLen = 0
    data = b''
    while True:
        readData = sock.recv(totalLen - readLen)
        readLen += len(readData)
        if readLen == totalLen:
            break
        return data.decode()


#  服务客户端的线程
def client(sock, addr):
    # 读取文件名长度
    strData = readByLen(sock, 8)
    totalLen = int(strData)  # 00000025--->25
    print('filename len is',totalLen)

    # 读文件名
    filename = readByLen(sock, totalLen)
    print('filename is', filename)
    oFile = open(filename, 'wb')

    # 读取文件内容长度
    strData = readByLen(sock, 8)
    totalLen = int(strData)
    print('file len is', totalLen)

    # 读取文件内容
    readLen = 0
    while True:
        readData = sock.recv(4096)
        oFile.write(readData)
        readLen += len(readData)
        if readLen == totalLen:
            break
    oFile.close()
    sock.close()

#  接收数据
def fileServerThread():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('', 10086))
    server.listen(250)
    print('文件服务器已经启动')

    while True:
        sock, addr = server.accept()
        print('接收连接')
        thread = Thread(target=client, args=(sock, addr))
        thread.start()


