from threading import Thread
import time
import os

'''
    1.线程是分配计算机＜内核＞的最小单位，它的其他资源来自于进程
(进程是分配计算机＜资源＞的最小单位)
    2.进程是资源分配的最小单位，线程是程序执行的最小单位
    3.进程有自己的独立地址空间，每启动一个进程，系统就会为它分配地址空间，
建立数据表来维护代码段、堆栈段和数据段，这种操作非常昂贵
而线程是共享进程中的数据的，使用相同的地址空间
因此CPU切换一个线程的花费远比进程要小很多，同时创建一个线程的开销也比进程要小很多
    4.线程之间的通信更方便，同一进程下的线程共享全局变量、静态变量等数据
而进程之间的通信需要以通信的方式（IPC)进行。不过如何处理好同步与互斥是编写多线程程序的难点

# 创建线程对象
t = Thread()
# target 绑定线程函数
# args 元祖　给线程函数传参
# kwargs 字典　给线程函数关键字传参
# 启动线程
t.start()
# 阻塞等待回收线程
t.join([timeout])

'''


def music():
    print(os.getpid())
    for i in range(5):
        time.sleep(1)
        print('+=%s=+'%i)

# 创建线程对象,下面创建的是分支线程.运行本py文件的线程是主线程
t = Thread(target=music, name='play_music')
print(t)
print(t.is_alive())
print(t)
t.start()
print(t.is_alive())
# 主线程
for i in range(3):
    print(os.getpid())
    time.sleep(1)
    print('qq')
t.join()  # 回收线程,一般会自动销毁


# def fun(sec,name):
#     print('线程函数传参')
#     time.sleep(sec)
#     print('%s完毕'%name)
#
# # 创建多个线程,多个线程各自执行
# th = []
# for i in range(5):
#     t = Thread(target=fun,args=(i,'QQ'))
#     t.start()
#     th.append(t)
#
# for i in th:
#     i.join()