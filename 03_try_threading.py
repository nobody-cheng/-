# coding=utf-8
import threading
import time
import multiprocessing

def fun():
    time.sleep(5)
    print("子进程程结束")

if __name__ == '__main__':
    # t1 = multiprocessing.Process(target=fun)
    t2 = threading.Thread(target=fun)
    # t1.setDaemon(True) #变成守护线程，当前这个守护线程不重要，主线程结束立马子线程也会结束

    # t1.start()
    # t1.join()
    t2.start()
    t2.join()
    print("主进程结束")