from socket import *
from threading import Thread

# 1.服务端地址
HOST = '0.0.0.0'
PORT = 8899
ADDR = (HOST, PORT)


# 4.处理客户端请求
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
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(ADDR)
s.listen(5)

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

    # 创建分支线程处理客户端请求
    t = Thread(target=handle, args=(c,))
    t.setDaemon(True)  # 主线程退出分支线程也会随之退出
    t.start()
