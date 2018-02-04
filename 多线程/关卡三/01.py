import threading
path = '/home/python/Desktop/test'
file = '*'


def Copy():
    cp file

t = threading.Thread(target=Copy)
t.start()
# send 192.168.17.255 有人回应下不