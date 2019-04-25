from multiprocessing import Process
from time import sleep


# 带参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm %s" % (name))
        print("I'm working...")


# p = Process(target=worker, args=(2, 'Eward'))
p = Process(target=worker, kwargs={'sec':2, 'name':'Eward'})

p.start()
p.join()
