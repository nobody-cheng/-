from socket import *
import uuid
import getpass

import fqcore
import fq

'''
fqnet.py: 负责网络初始化
          负责用户信息初始化
          负责发送数据
          负责接收数据
        
'''

# 2. 初始化网络
print("2. 初始化网络")
# 当fq运行时，uuid就是这个程序的身份证
uuid = str(uuid.uuid1())
# 获取机器账户名字，当飞球的用户名
name = getpass.getuser()
# 指定的端口
port = 20099
# 广播IP地址
boardcastIP = '192.168.17.255'

# 初始化socket，用于通信
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

print("2. 初始化网络结束")


# 发送一个字典
def sendDict(d, ip=boardcastIP):
    data = str(d).encode()
    sock.sendto(data, (ip, port))


# 发送上线消息
def online():
    # 发送上线信息
    onlineMsg = {
        fqcore.cmd: fqcore.online,
        fqcore.name: name,
        fqcore.uuid: uuid
    }
    sendDict(onlineMsg)


# 发送下线消息
def offline():
    # 发送上线信息
    offlineMsg = {
        fqcore.cmd: fqcore.offline,
        fqcore.uuid: uuid
    }
    sendDict(offlineMsg)


def onlineack(ip):
    onlineackMsg = {
        fqcore.cmd: fqcore.onlineack,
        fqcore.name: name,
        fqcore.uuid: uuid
    }
    sendDict(onlineackMsg, ip)


def setname(n):
    global name
    name = n

    setnameMsg = {
        fqcore.cmd: fqcore.setname,
        fqcore.name: name,
        fqcore.uuid: uuid
    }
    sendDict(setnameMsg)


# 获得网络输入，并且处理
def getNetworkData():
    print("7. 获取网络数据的子线程进入循环")
    # 不停的获取网络数据
    while True:
        # 接收网络数据，recvfrom会阻塞（卡在这里），一直到有其他feiQ发送消息过来
        data, addr = sock.recvfrom(8192)
        # 把网络数据变成字典：解包
        recvPack = eval(data.decode())
        # 把报文发给fq模块处理
        ret = fq.handleNetwork(recvPack, addr[0])
        if ret == False:
            break




