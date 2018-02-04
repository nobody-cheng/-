import time
import threading


def sorry():
    time.sleep(1)
    print('so soory')

for i in range(8):
    t = threading.Thread(target=sorry)
    t.start()

time.sleep(2)