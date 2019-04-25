from socket import *
from multiprocessing import Process
import signal

# 1.服务端地址
HOST = '0.0.0.0'
PORT = 8889
ADDR = (HOST, PORT)


# 5.处理客户端请求
def handle(connfd):
    print('Connect from:', connfd.getpeername())
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'OK')
    connfd.close()


# 2.创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)  # 设置端口复用
s.bind(ADDR)
s.listen(5)

# 6.处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

# 3.循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        break
    except Exception as e:
        print(e)
        continue

    # 4.创建子进程处理客户端请求
    p = Process(target=handle, args=(c,))
    p.daemon = True  # 主进程退出子进程也会随之退出
    p.start()
