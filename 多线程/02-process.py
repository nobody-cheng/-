import time
import threading
import multiprocessing
import os


def run():
    while True:
        time.sleep(0.8)
        print('that run', os.getpid())

process = multiprocessing.Process(target=run)
process.start()

while True:
    time.sleep(1)
    print('this run', os.getpid())

process.join()