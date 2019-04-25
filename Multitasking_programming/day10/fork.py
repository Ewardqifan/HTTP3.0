import os
import time

# 创建新的进程，生成整数，<0失败　＝0新进程　　>0老进程
pid = os.fork()

if pid < 0:
    print('Create process failed')
elif pid == 0:
    time.sleep(1)
    print('The new process')
else:
    time.sleep(3)
    print('The old process')

print('Fork test over')
