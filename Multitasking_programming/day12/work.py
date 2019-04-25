'''
　作业：
    1.效率测试
        def count(x,y):
            c = 0
            while c < 7000000:
                x += 1
                y += 1
                c += 1
        单进程(线程)运算　　10次
        10个进程(线程)     1次
        def write():
            f = open('test','w')
            for i in range(1500000):
                f.write('hello world\n')
        def read():
            f = open('test')
            f.readlines()
        def io():
           write()
           read()

        单进程(线程)运算　　10次
        10个进程(线程)    1次

    2.对比进程线程的联系与区别

    3.网络内容复习一下(socket重点程序)
'''
# 作业1

from multiprocessing import Process
from threading import Thread
import time


def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


def write():
    f = open('test', 'w')
    for i in range(1500000):
        f.write('hello world\n')


def read():
    f = open('test')
    f.readlines()


def io():
    write()
    read()


'''
# ======================
#       单进程
# ======================
t1 = time.time()
for i in range(10):
    count(0, 0)
print('计算密集型单进程时间:%.4f' % (time.time() - t1))

t11 = time.time()
for n in range(10):
    io()
print('IO单进程时间:%.4f' % (time.time() - t11))


# ======================
#       多进程
# ======================
def process_test(count, args=()):
    process = []
    t = time.time()
    for j in range(10):
        p = Process(target=count, args=args)
        p.start()
        process.append(p)
    for i in process:
        i.join()
    return time.time() - t


print('计算密集型多进程时间:%.4f' % process_test(count, args=(0, 0)))
print('IO多进程时间:%.4f' % process_test(io))
'''

# ======================
#       单线程
# ======================
t22 = time.time()
for times in range(10):
    t = Thread(target=count, args=(0, 0))
    t.start()
    t.join()
print('|计算密集型| >单线程< 时间:%.4f' % (time.time() - t22))

t33 = time.time()
for times_01 in range(10):
    t = Thread(target=io)
    t.start()
    t.join()
print('|IO密集型| >单线程< 时间:%.4f' % (time.time() - t33))


# ======================
#       多线程
# ======================
def thread_test(target, args=()):
    start_time = time.time()
    th = []
    for times in range(10):
        t = Thread(target=target, args=args)
        t.start()
        th.append(t)
    for i in th:
        i.join()
    return time.time() - start_time


print('|计算密集型| >多线程< 时间:%.4f' % (thread_test(count, args=(0, 0))))
print('|IO密集型| >多线程< 时间:%.4f' % (thread_test(io)))

'''
|计算密集型| >单线程< 时间:7.0753
|IO密集型| >单线程< 时间:4.9027
|计算密集型| >多线程< 时间:7.0586
|IO密集型| >多线程< 时间:4.0423
'''

'''
|计算密集型| >单进程< 时间:7.4856
|IO密集型| >单进程< 时间:6.7218
|计算密集型| >多进程< 时间:3.9943
|IO密集型| >多进程< 时间:2.1467
'''

