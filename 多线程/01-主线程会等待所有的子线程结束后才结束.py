import threading
import time


# def sing():
#     for i in range(5):
#         print('正在唱歌。。。%d' % i)
#         time.sleep(1)
#
#
# def dance():
#     for i in range(5):
#         print('正在跳舞。。。%d' % i)
#         time.sleep(1)
#
# if __name__ == '__main__':
#     print('====开始===')
#
#     t1 = threading.Thread(target=sing)
#
#     t2 = threading.Thread(target=dance)
#
#     t1.start()
#     t2.start()
#
#     time.sleep(5)
# print('===结束===')


def sing():
    for i in range(5):
        print('正在唱歌。。。%d' % i)
        time.sleep(1)


def dance():
    for i in range(5):
        print('正在跳舞。。。%d' % i)
        time.sleep(1)


if __name__ =='__main__':

    print('程序开始执行')
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    t1.start()
    t2.start()
    time.sleep(5)
print('程序结束')
