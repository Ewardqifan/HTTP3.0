import os
from time import sleep, time


def buissness01():
    sleep(3)
    print('垆边人似月')


def buissness02():
    sleep(4)
    print('皓腕凝霜雪')


# 父进程
t1 = time()

pid = os.fork()
if pid == 0:  # 一级子进程
    ppid = os.fork()
    if ppid == 0:  # 二级子进程
        buissness01()
    else:
        os._exit(0)
elif pid < 0:
    print('创建一级子进程失败')
else:  # 父进程回收一级子进程 结果是父进程和二级子进程同时运行
    pid, status = os.wait()
    buissness02()

print(time() - t1)
