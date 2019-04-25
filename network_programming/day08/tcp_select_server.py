from select import select
from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
sockfd.bind(('0.0.0.0', 8000))
sockfd.listen(3)  # 监听阻塞操作

# IO关注列表
rlist = [sockfd]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    # 分别是'读','写','异常'三种io操作
    for r in rs:
        if r == sockfd:
            connfd, addr = sockfd.accept()
            print('Connect from', addr)
            rlist.append(connfd)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print('Have recivered msg from', r.getpeername())
            wlist.append(r)
    for w in ws:  # '写'操作代表了主动处理的io操作
        w.send(b'Reciver your message')
        wlist.remove(w)
    for x in xs:
        pass
