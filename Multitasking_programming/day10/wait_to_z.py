import os
from time import sleep

pid = os.fork()

if pid == 0:
    sleep(1)
    print('Subprocess %d exit' % (os.getpid()))
    os._exit(10)  # 退出状态为0默认为0
else:
    # os.wait处理该父进程下的僵尸进程
    # pid, status = os.wait()
    # wait的非阻塞模式
    pid , status = os.waitpid(-1,os.WNOHANG)
    # pid为处理的僵尸进程的pid
    # status为处理子进程的退出状态，一般为exit函数传入值乘256
    print('Subprocess PID:%d | status:%d' % (pid, status / 256))
    while True:
        sleep(100)
        break
