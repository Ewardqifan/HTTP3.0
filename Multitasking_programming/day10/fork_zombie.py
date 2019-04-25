import os
from time import sleep

pid = os.fork()

if pid == 0:
    print('Subprocess PID:', os.getpid())
    os._exit(0)
else:
    print('PPID:', os.getpid())
    while True:
        pass  # 保持父进程
