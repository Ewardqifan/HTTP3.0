'''
    多进程服务端建立,父进程一直监听,有连接就建立子进程处理
    注意的点:不断的建立子进程需要处理僵尸进程
'''
from socket import *
import os, sys
import signal

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(ADDR)
s.listen(5)

# 交给操作系统进行处理,僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)


# 处理客户端请求函数
def client_handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'OK')
    c.close()


# 1.循环等待客户端连接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit('服务器退出')
    except Exception as e:
        print(e)
        continue

    # 2.创建子进程
    pid = os.fork()
    if pid == 0:
        s.close()  # 子进程关闭原套接字
        client_handle(c)  # 3.处理客户端请求
        os._exit(0)  # 退出子进程
    else:
        c.close()  # 父进程关闭连接套接字
        continue
