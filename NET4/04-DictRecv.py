from socket import *
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', 10099))

data, addr = sock.recvfrom(1024)

data = data.decode()
# print(data)
d = eval(data)

print('ip=%s, uuid=%s,name=%s' % (addr[0], d['uuid'], d['name']))
