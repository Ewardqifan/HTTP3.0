from multiprocessing import Process
from time import sleep, ctime


def fun():
    for i in range(3):
        sleep(2)
        print(ctime())


p = Process(target=fun, name='Tedu')

# p.daemon = True  # 父进程退出子进程也会随之退出

p.start()

print('Nanme:', p.name)
print('PID:', p.pid)
print('alive:', p.is_alive())

p.join()  # 阻塞函数....
