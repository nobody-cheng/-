# 03-task_master.py
import random, time, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue,所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接服务器,即主机
server_addr = '127.0.0.1'
# 端口和验证码注意保持与task_master.py一致
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接
m.connect()
# 获取queue对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列获取任务,把结果写入result
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty')
# 处理结束:
print('worker exit.')

