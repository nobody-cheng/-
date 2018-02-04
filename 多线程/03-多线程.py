import threading
import time


def sing():
    for i in range(5):
        print('正在唱歌。。。%s' % i)
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞。。。%d' % i)
        time.sleep(1)

t1 = threading.Thread(target=sing)
t2 = threading.Thread(target=dance)

t1.start()
t2.start()
# dance()

# t1.join()