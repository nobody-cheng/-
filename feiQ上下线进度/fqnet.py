from socket import *
import uuid
import getpass
import threading
import fq
import fqcore

'''
负责网络初始化
负责用户信息初始化
负责发送数据
负责接收数据

'''

# 获取主机名
name = getpass.getuser()
# 获取唯一ID
uuid = str(uuid.uuid1())
# 绑定端口
port = 10086
# 广播地址
braodcastIP = '192.168.17.255'
# 创建套接字
sock = socket(AF_INET, SOCK_DGRAM)
# 绑定端口
sock.bind(('', port))
# 广播
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


# 发送字典
def sendDict(d, ip=braodcastIP):
    # 编码
    data = str(d).encode()
    sock.sendto(data, (ip, port))


# 上线消息
def online():
    onlineMsg = {fqcore.cmd: fqcore.online, fqcore.uuid: uuid, fqcore.name: name}
    # data = str(onlineMsg).encode()
    # sock.sendto(data, (braodcastIP, port))
    sendDict(onlineMsg)


# 下线消息
def offline():
    offlineMsg = {fqcore.cmd: fqcore.offline, fqcore.uuid: uuid}
    # data = str(offlineMsg).encode()
    # sock.sendto(data, (braodcastIP, port))
    sendDict(offlineMsg)


# 回应消息
def onlineack(ip):
    onlineackMsg = {fqcore.cmd: fqcore.onlineack, fqcore.name: name, fqcore.uuid: uuid}
    sendDict(onlineackMsg, ip)


def setname(n):
    global name
    name = n
    setnameMsg = {fqcore.cmd: fqcore.setname, fqcore.name: name, fqcore.uuid: uuid}
    sendDict(setnameMsg)


def sendMsg(ip, msg):
    speakMsg = {fqcore.cmd: fqcore.msg, fqcore.msg: msg, fqcore.uuid: uuid, fqcore.name: name}
    sendDict(speakMsg, ip)


def getnetworkData():
    # 不断获取网络数据
    while True:
        # 不断接收网络数据，recvfrom阻塞，直到有新的fq消息进来
        data, addr = sock.recvfrom(1024)
        # 把网络数据变成字典，解包
        recvPack = eval(data.decode())
        # 报文给fq模块处理
        ret = fq.handleNetwork(recvPack, addr[0])
        if ret == False:
            break