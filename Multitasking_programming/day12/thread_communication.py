'''
    线程通信：
    通过进程(进程间有所有线程共用的全局变量)
    为了解决线程间用于的共享资源被其他线程占用的情况，提出同步互斥机制
    ps：共享资源，多个进程和线程都可以操作的资源
        对共享资源的无序操作可能带来数据混乱
'''

from threading import Event, Thread
import time

'''
e = Event()# 创建线程Event对象
e.wait([timeout])# 阻塞等待直到e被set
e.set()# 设置e，使wait结束阻塞
e.clear()# 清除e的设置，wait为阻塞
e.is_set()#　判断e的状态查看是否没set
'''

# e = Event()
# e.wait(3)  # 相当于上锁，如果不设置timeout则会一直阻塞
# print(e.is_set())
# e.set() # 相当于解锁
# print(e.is_set())

'''
s = None  # 用于通讯的全局变量


def test01():
    time.sleep(0.1)
    print('=============')
    global s
    s = '孤帆远影碧空尽'


# 分支线程
f = Thread(target=test01, name='上阙')
f.start()

if s == '孤帆远影碧空尽':
    print('唯见长江天际流')
else:
    print('>>fail<<')

f.join()

# 无法交流，主线程和分支线程都操作s，而主线程先收到s==None
'''
'''
s = None  # 用于通讯的全局变量
e = Event()
def test01():
    time.sleep(0.1)
    global s
    s = '孤帆远影碧空尽'
    e.set()
# 分支线程
f = Thread(target=test01, name='上阙')
f.start()
e.wait() # 在判断全局变量时加入 >>锁<< ，在分支进程中解除 >>锁<<
if s == '孤帆远影碧空尽':
    print('唯见长江天际流')
else:
    print('>>fail<<')
f.join()
'''

'''
from threading import Lock
lock = Lock()  # 创建锁
lock.acquire()  # 上锁;如果已经上锁,则阻塞
lock.release()  # 解锁
with lock: 上锁
    XXXXXXX
'''

from threading import Thread, Lock

lock = Lock()
a = b = 0


def value():
    while True:
        lock.acquire()
        if a != b:
            print('a=%d,b=%d' % (a, b))
        lock.release()

t = Thread(target=value)

t.start()

while True:
    with lock:
        a += 1
        b += 1

t.join()
