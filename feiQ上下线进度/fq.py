
import uuid
import threading

import os
import fqcore
import fqnet
import fquser
"""
主程序，负责上线，下线等业务处理
       负责线程创建
       负责用户输入
       负责所有的业务处理
"""


def handleNetwork(recvPack, ip):

    if recvPack[fqcore.cmd] == fqcore.msg:
        if recvPack[fqcore.uuid] == fqnet.uuid:
            return True
        print('%s %s %s' % (recvPack[fqcore.name], ip, recvPack[fqcore.msg]))

    # 收到上线消息
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
        # if recvPack[fqcore.uuid] == fqnet.uuid:
        #     return True
        # print('%s %s %s 我也在线,欢迎来撩' % (recvPack[fqcore.name], recvPack[fqcore.uuid], ip))
        fquser.addUser(recvPack[fqcore.name], recvPack[fqcore.uuid], ip)

    elif recvPack[fqcore.cmd] == fqcore.offline:
        # 收到自己的下线，返回false让子线程退出
        if recvPack[fqcore.uuid] == fqnet.uuid:
            return False
        # 收到别人的下线消息，调用fquser删除一个账户
        fquser.removeUser(recvPack[fqcore.uuid])

    elif recvPack[fqcore.cmd] == fqcore.setname:
        # 修改用户名
        if recvPack[fqcore.uuid] == fqnet.uuid:
            return True
        fquser.changeName(recvPack[fqcore.uuid],recvPack[fqcore.name])


def main():
    # 上线
    fqnet.online()
    # 创建子线程，处理网络数据
    thread = threading.Thread(target=fqnet.getnetworkData)
    # 启动子线程
    thread.start()

    # 获取键盘输入
    while True:
        # 获取用户输入
        data = input('feiQ:  ')
        # 去掉前后空格
        data = data.strip()

        if data.startswith('send '):
            datas = data.split(' ', 2)
            #(send ip msg)
            if len(datas) < 3:
                print('  命令错误：send {ip} {msg}')
                continue
            fqnet.sendMsg(datas[1], datas[2])

        elif data == 'users':
            fquser.outputUserList()

        elif data.startswith('setname '):
            datas = data.split(' ', 1)
            datas[1] = datas[1].strip()
            if datas[1].find(' ') != -1:
                print('  名字中不能带空格')
                continue
            fqnet.setname(datas[1])

        elif data == 'clear':
            os.system('clear')

        elif data == 'whoami':
            print(fqnet.name, fqnet.uuid)

        elif data == 'exit':
            break

        else:
            print("  输入错误，请按格式输入")
            print("  发送消息:  send + {ip} + {msg} ")
            print("  修改名字:  setname + newname")
            print("  退出:  exit")
            print("  查看列表:  users")
            print("  清屏:  clear")

    # 发送下线广播
    fqnet.offline()
    thread.join()

if __name__ == '__main__':
    main()
