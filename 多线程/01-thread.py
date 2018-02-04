import time
import threading
import os
import multiprocessing

def run():
    while True:
        time.sleep(0.8)
        print('that run', os.getpid())  # 获得进程号

thread = threading.Thread(target=run)
thread.start()

while True:
    time.sleep(1)
    print('this run', os.getpid())

thread.join()