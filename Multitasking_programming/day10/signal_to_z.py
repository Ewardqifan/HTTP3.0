'''
信号方法处理僵尸进程：
子进程退出会给父进程发送信号，如果父进程忽略，则自动交给操作系统处理子进程退出
非阻塞,可以处理所有子进程退出
'''

import signal
import os
import time

# signal.SIGCHLD --> 向父进程发送信号
# signal.SIG_IGN --> 父进程忽略处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

pid = os.fork()

if pid < 0 :
    print('Error')
elif pid == 0:
    print('Stop:',os.getpid())
else:
    while True:
        time.sleep(100)
