'''
进程池技术
    进程的创建和和销毁占用许多计算机资源当任务小而多的时候进程池技术就很好用
    通过创建一定数量的进程来处理事件，事件处理腕进程不退出而是继续处理其他时间
    事件处理完一同处理
'''

from multiprocessing import Pool
import time

def worker(arg):
    time.sleep(2)
    print(arg)

# 创建进程池
po = Pool()
print(po._processes)
for i in range(10):
    msg = 'hello %d'%i
    po.apply_async(worker,args=(msg,)) #apply_async 异步调用

po.close() #　先关闭后回收
po.join()
