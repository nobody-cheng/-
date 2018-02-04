"""
使用threading模块中的Thread，创建2个子线程
线程1中每秒钟打印1个A，线程2中每2秒钟打印1个B
"""

import threading
import time


def func1():
    for i in range(10000):
        print('A')
        time.sleep(1)


def func2():
    for i in range(10000):
        print('B')
        time.sleep(2)

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()