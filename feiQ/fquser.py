# 用户列表
users = []


# 封装用户
class User():
    def __init__(self,name, uuid, ip):
        self.name = name
        self.uuid = uuid
        self.ip = ip


# 添加用户到列表
def addUser(name, uuid, ip):
    user = User(name, uuid, ip)
    users.append(user)


# 打印用户列表
def outputUserList():
    if len(users) == 0:
        print('  not user')
    for user in users:
        print('user:  %s %s %s' % (user.name, user.uuid, user.ip))


# 删除用户账户
def removeUser(uuid):
    for user in users:
        if user.uuid == uuid:
            users.remove(user)
            break


def changeName(uuid, name):
    for user in users:
        if user.uuid == uuid:
            user.name = name
            break


