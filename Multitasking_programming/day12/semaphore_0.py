'''
 信号量控制
    通信原理：给定一个数量对多个进程可见
            多个进程都可以操作数量的增减
            并根局数量决定行为
'''
'''
from multiprocessing import Semaphore

# 创建信号量对象
sem = Semaphore(num)
# num代表信号量初始值
sem.acquire()  # 消耗一个信号量，当信号量为0时会阻塞
sem.release()  # 增加一个信号量
sem.get_value()  # 获取一个信号量的值
'''

from multiprocessing import Semaphore, Process
from time import sleep
import os

# 创建信号量
sem = Semaphore(3)  # 共有三个信号量


# 创建进程事件 --> 要求:最多有三个进程同时执行该事件
def fun():
    sem.acquire()  # 捕获一个信号量
    print('%d执行' % os.getpid())
    sleep(3)
    print('%d完毕' % os.getpid())
    sem.release()  # 释放一个信号量


process = []
for i in range(5):
    p = Process(target=fun)
    p.start()
    process.append(p)

for i in process:
    i.join()
