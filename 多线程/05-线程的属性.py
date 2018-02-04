import threading
import time

def threadFunc():
    print(threading.current_thread().getName())

# thread = threading.Thread(target=threadFunc)
# print(dir(thread))
#print(thread.getName())
# thread.start()

# thread = threading.Thread(target=threadFunc, name='hello')
#print(thread.getName())
# thread.start()

thread = threading.Thread(target=threadFunc)
#print(thread.getName())
# thread.start()

time.sleep(1)
#thread.join()
print("alive is:", thread.isAlive())

threadFunc()