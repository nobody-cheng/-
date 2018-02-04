from socket import *
import uuid
import getpass
import threading

import fqcore

users = []

# 获取主机名
name = 'Windows'
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


class User():
    def __init__(self,name, uuid, ip):
        self.name = name
        self.uuid = uuid
        self.ip = ip


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
    onlineackMsg = {fqcore.cmd: fqcore.online, fqcore.name: name, fqcore.uuid: uuid}
    sendDict(onlineackMsg, ip)


def addUser(name, uuid, ip):
    user = User(name, uuid, ip)
    users.append(user)

def outputUserList():
    if len(users) == 0:
        print('not user')
    for user in users:
        print('user:  %s %s %s' % (user.name, user.uuid, user.ip))

online()


def getnetworkData():
    # 不断获取网络数据
    while True:
        # 不断接收网络数据，recvfrom阻塞，直到有新的fq消息进来
        data, addr = sock.recvfrom(1024)
        # 解包
        recvPack = eval(data.decode())
        # 收到上线消息
        if recvPack[fqcore.cmd] == fqcore.online:
            # 收到自己上线消息，continue
            if recvPack[fqcore.uuid] == uuid:
                return
            # 收到别人上线消息，添加到一个列表中
            addUser(recvPack[fqcore.name], recvPack[fqcore.uuid], addr[0])
            # 回应消息
            onlineack(addr[0])
        if recvPack[fqcore.cmd] == fqcore.onlineack:
            addUser(recvPack[fqcore.name], recvPack[fqcore.uuid], addr[0])
# 创建子线程，处理网络数据
thread = threading.Thread(target=getnetworkData)
# 启动子线程
thread.start()

# 获取用户输入
while True:
    data = input('feiQ:  ')
    if data == 'users':
        outputUserList()



thread.join()