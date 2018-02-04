
import time
import multiprocessing
import threading
import os

# 多进程的全局变量，是不共享的
# py代码运行的进程叫做父进程
# Process创建的进程叫做子进程
num = 0

def fun():
    pass

def run100():
    global num
    time.sleep(0.8)
    num = 200
    fun()

process = multiprocessing.Process(target=run100)
process.start() # 启动子进程：run100函数开始执行

num = 100
fun()

process.join()

print('num is', num)