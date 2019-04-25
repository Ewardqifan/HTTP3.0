'''
看下HTTP
复习文件操作
使用select完成一个服务端：
要求将客户端发来的信息写入日志文件
同时服务端接受终端输入内容，(sys.stdin.readline)也写入到日志中
'''

from select import select
from socket import *
import sys

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

sockfd.bind(('0.0.0.0', 8800))

sockfd.listen(3)

rlist = [sockfd, sys.stdin]
wlist = []
xlist = []

while True:
    rs, ws, xs = select(rlist, wlist, xlist, 5)
    for r in rs:
        if r == sockfd:
            connfd, addr = r.accept()
            print('连接成功,地址：', addr)
            rlist.append(connfd)
        elif r == sys.stdin:
            data = r.readline()
            data = data[:-1] # readline会把最后一个回车写入,这里去掉
            # print('输入e:%s'%(data))
            data += '  --from terminal\r'
            f = open('log.txt', 'a')
            f.write(data)
            f.flush()
            f.close()
        else:
            print('等待接收消息')
            data = r.recv(4096)
            if not data:
                print('接受完毕')
                rlist.remove(r)
                r.close()
                break
            print('Reciver msg from:', r.getpeername())

            r.send(b'OK')
            f = open('log.txt', 'ab')
            data += b'  --from client\r\n'
            f.write(data)
            f.flush() # 将写入缓存的内容放入磁盘清理缓存
            f.close()
    for w in ws:
        pass
    for x in xs:
        pass
