import uuid
import getpass
import time
import threading
import os

import fqcore
import fqnet
import fquser

'''
fq.py: 主程序，负责上线，下线等业务处理
       负责线程创建
       负责用户输入
       负责所有的业务处理
'''

def handleNetwork(recvPack, ip):

    if recvPack[fqcore.cmd] == fqcore.msg:
        if recvPack[fqcore.uuid] == fqnet.uuid:
            return True

        msg = recvPack[fqcore.msg]
        print(("%s(%s)say:%s") % (recvPack[fqcore.name], ip, msg))

    elif recvPack[fqcore.cmd] == fqcore.online:
        # 收到自己发的上线，就不处理
        if recvPack[fqcore.uuid] == fqnet.uuid:
            return True

        # 如果收到别人的上线信息，那么把这些信息，构造一个User对象，并us保存到users列表
        fquser.addUser(recvPack[fqcore.name], ip, recvPack[fqcore.uuid])
        # 回应我也在线
        fqnet.onlineack(ip)

        print("%s %s %s 上线啦" % (recvPack[fqcore.name], recvPack[fqcore.uuid], ip))

    elif recvPack[fqcore.cmd] == fqcore.onlineack:
        fquser.addUser(recvPack[fqcore.name], ip, recvPack[fqcore.uuid])

    elif recvPack[fqcore.cmd] == fqcore.offline:
        # 自己发给自己的offline，返回False让子线程退出
        if recvPack[fqcore.uuid] == fqnet.uuid:
            return False

        # 收到别人发出来的offline，调用fquser删除一个账户
        fquser.removeUser(recvPack[fqcore.uuid])

    elif recvPack[fqcore.cmd] == fqcore.setname:
        # 收到自己发的上线，就不处理
        if recvPack[fqcore.uuid] == fqnet.uuid:
            return True
        fquser.changeName(recvPack[fqcore.uuid], recvPack[fqcore.name])

    return True

def sendMsg(ip, msg):
    #
    # {
    #   'cmd': 'msg'
    #   'msg': 'hello world'
    #   'uuid': 'asdfsfadfadfadf'
    #   'name': name
    # }
    #
    d = { fqcore.cmd: fqcore.msg, fqcore.msg: msg, fqcore.uuid: fqnet.uuid, fqcore.name: fqnet.name}

    fqnet.sendDict(d, ip)


def main():

    # 4. 告诉所有人，新用户上线
    # 一开始上线
    print("4. 告诉所有人，新用户上线")
    fqnet.online()

    print("5. 启动网络数据处理线程")
    # 创建子线程，在子线程处理网络数据
    thread = threading.Thread(target=fqnet.getNetworkData)
    thread.start()

    print("6. 主线程进入循环")
    # 获取用户键盘输入，然后发送消息
    while True:
        # 获取用户键盘输入，input也会阻塞，一直到用户有输入内容
        data = input('feiQ: ')
        # 去掉前后空格
        data = data.strip()

        if data.startswith('send '):
            datas = data.split(' ', 2)
           # [1, 2, 3]
            if len(datas) < 3:
                print('  命令错误: send {ip} {msg}')
                continue
            sendMsg(datas[1], datas[2])

        # 健壮性
        elif data == 'clear':
            os.system('clear')

        elif data == 'users':
            fquser.outputUserList()

        elif data.startswith('setname '):
            datas = data.split(' ', 1)
            datas[1] = datas[1].strip()
            if datas[1].find(' ') != -1:
                print('  名字中不能带空格')
                continue

            fqnet.setname(datas[1])

        elif data == 'exit':
            break



    # 发送下线广播
    fqnet.offline()
    thread.join()

if __name__ == '__main__':

    main()

