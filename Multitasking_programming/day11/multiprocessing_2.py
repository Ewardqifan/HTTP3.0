from multiprocessing import Process  # 创建的子进程无法使用input和一些标准输入
from time import sleep, time
import os


def th1():
    sleep(3)
    print('吃饭')
    print(os.getppid(), '---', os.getpid())


def th2():
    sleep(2)
    print('睡觉')
    print(os.getppid(), '---', os.getpid())


def th3():
    sleep(4)
    print('打豆豆')
    print(os.getppid(), '---', os.getpid())


things = [th1, th2, th3]
process = []
t1 = time()
for th in things:
    p = Process(target=th)
    process.append(p)  # 使用列表保存进程对象
    p.start()

print(time() - t1)

for i in process:  # 循环回收对象
    i.join()
