import gevent
from gevent import monkey

monkey.patch_all()  # 需要在导入有阻塞的模块之间调用
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
s.bind(('0.0.0.0', 8888))
s.listen(5)


# 处理请求函数
def handle(connfd):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')


# 循环连接客户端
while True:
    try:
        c, addr = s.accept()
        print('Connect from:', addr)
    except KeyboardInterrupt:
        s.close()
        break
    except Exception as e:
        print(e)
        continue
    # 创建协程处理连接:循环连接部分的accept为阻塞状态
    # C是不同的参数,会多次调用handle函数.
    # 因此只要调用一次handle就会启动一个协程程序
    gr = gevent.spawn(handle, c)
s.close()
