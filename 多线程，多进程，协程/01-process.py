import os, time, random
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue

# print('Process %s start...' % os.getpid())
# pid = os.fork()  # 创建子进程返回0
# print(pid)
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
print('*' * 100)


# def run_process(name):
#     print('run child process %s  (%s)...' % (name, os.getpid()))
# if __name__ == '__main__':
#     print('Parent process %s' % os.getpid())
#     p = Process(target=run_process, args=('test',))
#     print('child process will start')
#     p.start()
#     p.join()
#     print('child process end')

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
#
# if __name__ == '__main__':
#     print('parent process %s' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')
def write(q):
    """以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据"""
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue..'%value)
if __name__ == '__main__':
    q=Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()
"""
在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调
用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程
去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了
在Unix/Linux下，可以使用fork()调用实现多进程。
要实现跨平台的多进程，可以使用multiprocessing模块。
进程间通信是通过Queue、Pipes等实现的。
"""