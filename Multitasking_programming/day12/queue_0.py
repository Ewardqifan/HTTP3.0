from multiprocessing import Queue,Process
from time import sleep

q = Queue(3)

# 创建消息队列
def fun1():
    for i in range(3):
        sleep(1)
        q.put((1,1))

def fun2():
    for i in range(4):
        try:
            a,b = q.get(timeout = 3)
        except:
            return
        print('sum = ',a+b)

process = []
th = [fun1,fun2]

for i in th:
    p = Process(target=i)
    p.start()
    process.append(p)

for i in process:
    i.join()