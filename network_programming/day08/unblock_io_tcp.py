from socket import *
from time import ctime, sleep

sockefd = socket()
sockefd.bind(('127.0.0.1', 8000))
sockefd.listen(5)

# sockefd.setblocking(False)  # 设置非阻塞io操作
sockefd.settimeout(3) # 超时设置

while True:
    print('Waiting for connect')
    try:
        connfd, addr = sockefd.accept()
    except BlockingIOError or timeout:
        sleep(2)
        print('%s connectiong error'%ctime())
        continue
    else:
        print('Connect from',addr) #addr为元组形式而非字符串
