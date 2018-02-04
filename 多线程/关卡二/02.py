"""
创建2个子线程，线程1、2同时对全局变量num各加100万次操作（num初始值为0）
每次加1，最后执行完成打印结果
"""
import threading
mutex = threading.Lock()
num = 0


def add1():
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1
        mutex.release()


def add2():
    global num
    for i in range(1000000):
        mutex.acquire()
        num += 1
        mutex.release()
t1 = threading.Thread(target=add1)
t2 = threading.Thread(target=add2)

t1.start()
t2.start()

# add1()
# t1.join()
print(num)