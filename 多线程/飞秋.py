from socket import *
import time
import fqcore
import uuid
import getpass
import threading

uuid = str(uuid.uuid1())
name = getpass.getuser()
port = 10006
booardcastIP = '127.0.0.1'


class User:
    def __init__(self, name, uuid, ip):
        self.name =name
        self.uuid =uuid
        self.ip = ip



#  用户列表 不包含自身
users = []


#  创建套接字
sock = socket(AF_INET, SOCK_DGRAM)
#  绑定端口
sock.bind(('', port))
#  广播
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
#  发送消息
# sock.sendto('hello'.encode(), ('127.0.0.1', 10086))


def sendDict(msg, ip=booardcastIP):
    data = str(msg).encode()
    sock.sendto(data, (ip, port))


def online():
    onlineMsg = {fqcore.cmd: fqcore.online, fqcore.uuid: uuid, fqcore.name: name}

    sendDict(onlineMsg)


def offilne():
    offline = {fqcore.cmd: fqcore.offline, fqcore.uuid: uuid}

    sendDict(offline)


def onlineack(ip):
    #  回应消息
    onlineackMsg = {fqcore.cmd: fqcore.onlineack, fqcore.name: name, fqcore.uuid: uuid}
    sendDict(onlineackMsg, ip)


#  上线
online()

def addUser(name, ip, uuid):
    user =User(name, ip, uuid)
    users.append(user)

#  获得网络输入，处理
def getNetworkData():
    while True:
        #  接收消息,网络数据
        data, addr = sock.recvfrom(1024)
        #  解码解包
        recvPack = eval(data.decode())

        if recvPack[fqcore.cmd] == fqcore.online:
            #  收到自己上线消息，跳过不处理
            if recvPack[fqcore.uuid] == uuid:
                continue

            #  如果收到别人的上线信息，创建一个User对象，保存到users列表
            addUser(recvPack[fqcore.name], addr[0], recvPack[fqcore.uuid])

            # 回应在线消息
            onlineack(addr[0])
        if recvPack[fqcore.cmd] == fqcore.onlineack:
            addUser(recvPack[fqcore.name], addr[0], recvPack[fqcore.uuid])


#  创建子线程，在子线程处理网络数据
t = threading.Thread(target=getNetworkData)
t.start()

while True:
    #  获取用户键盘输入
    data = input('请输入：')

#  下线
offilne()
t.join()
