from socket import *
import time
import fqcore
import uuid
import getpass

uuid = str(uuid.uuid1())
name = getpass.getuser()
port = 10086
booardcastIP = '127.0.0.1'
#  创建套接字
sock = socket(AF_INET, SOCK_DGRAM)
#  绑定端口
sock.bind(('', 10086))
#  广播
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
#  发送消息
# sock.sendto('hello'.encode(), ('127.0.0.1', 10086))

def sendDict(msg):
    data = str(msg).encode()
    sock.sendto(data, (booardcastIP, port))


def online():
    onlineMsg = {fqcore.cmd: fqcore.online, fqcore.uuid: uuid, fqcore.name: name}

    sendDict(onlineMsg)


def offilne():
    offline = {fqcore.cmd: fqcore.offline, fqcore.uuid: uuid}

    sendDict(offline)

while True:
    #  接收消息
    data, addr = sock.recvfrom(1024)
    #  解码解包
    recvPack = eval(data.decode)

    if recvPack[fqcore.cmd] == fqcore.online:
        if recvPack[fqcore.uuid] == uuid:
            continue

        print('%s %s %s online' % (recvPack['name'], recvPack['uuid'], addr[0]))