import threading
import time


class MyThread(threading.Thread):
    def run(self):
        time.sleep(1)
        print('封装封装封装')

for i in range(8):
    t = MyThread()
    t.start()
