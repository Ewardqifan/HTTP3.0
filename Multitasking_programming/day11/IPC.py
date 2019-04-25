'''
进程间通讯(IPC,inter-process-communication) -- 例如套接字文件
eg:APP 之间帐号的通用
在操作系统的维度来看进程间的通信方法：
    管道/消息队列/共享内存/信号/信号量/套接字
'''

from multiprocessing import Pipe, Process  # 管道通信
import time, os

'''
# 创建管道
fd1,fd2 = Pipe(duplex=True)
# duplex　-->　True 代表双向管道 False 代表单向
# 单项下，fd1只读fd2只写;双向下,两个均可读写.

fd.recv() # 从管道读
fd.send(data) #向管道写
'''

fd1, fd2 = Pipe(True)


def fun(name):
    time.sleep(3)
    fd1.send({name: os.getpid()})


jobs = []
for i in range(5):
    p = Process(target=fun, args=(i,))
    jobs.append(p)
    p.start()

for i in range(5):
    data = fd2.recv()
    print(data)

for j in jobs:
    j.join()
