# task_master.py
import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务队列
task_queue = queue.Queue()
# 接收结果队列
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 吧两个Queue都注册到网络上,callable参数关联Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000,设置验证码abc:
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue
manager.start()
# 通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去
for i in range(10):
    n = random.randint(0, 100)
    print('Put task %d..' % n)
    task.put(n)
# 从result队列读取结果
print('Try get result..')
for k in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
manager.shutdown()
print('master exit')
