from socket import *
import os

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1', 10086))

filename = 'zhangcheng_test'

# 发送文件名长度
filenameData = filename.encode()
filenameLen = len(filenameData)
filenameLenStr = '%08d' % filenameLen
filenameLenData = filenameLenStr.encode()
sock.send(filenameLenData)
# 发送文件名
sock.send(filenameData)

# 发送文件内容长度
filename = '/home/python/Desktop/python高级-06-协程/zhangcheng_test'
filelen = os.path.getsize(filename)
filenameStr = '%08d' % filelen
filenameStrData = filenameStr.encode()
sock.send(filenameStrData)

def writeByData(sock, data):
    writeLen = 0
    while True:
        ret = sock.send(data[writeLen:])
        writeLen += ret
        if writeLen == len(data):
            break

# 发送问价内容
iFile = open(filename, 'rb')
while True:
    data = iFile.read(1024)
    if not data:
        break
    writeByData(sock, data)
iFile.close()

