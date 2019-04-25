import os
from time import sleep

pid = os.fork()  # 创建的子进程返回0，父进程返回子进程的pid号
if pid < 0:
    print('Error')
elif pid == 0:
    sleep(2)  # 孤儿进程
    print('===子进程===')
    print('PPID:', os.getppid())  # 获取父进程的PID号
    print('Subprocess:', os.getpid())  # 获取当前进程的PID号
else:
    print('===父进程===')
    print('PPID****:', os.getpid())
    print('Subprocess****:', pid)
