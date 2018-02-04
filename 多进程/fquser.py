'''
fquser: 负责用户数据结构抽象
        负责增加用户、删除用户、查找用户
'''
# 用户列表，不包含
# 3. 初始化用户列表
print("3. 初始化用户列表")
users = []


# 封装用户
class User:
    def __init__(self, name, uuid, ip):
        self.name = name
        self.uuid = uuid
        self.ip = ip

def addUser(name, ip, uuid):
    user = User(name, uuid, ip)
    users.append(user)


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


def outputUserList():
    if len(users) == 0:
        print("  no users")
        return

    for user in users:
        print("  user: %s %s %s" % (user.name, user.ip, user.uuid))
