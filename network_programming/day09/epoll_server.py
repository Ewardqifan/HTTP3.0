from select import *
from socket import *

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
sockfd.bind(('0.0.0.0', 8800))
sockfd.listen()

# epoll对象,多了一个EPOLLET事件
p = epoll()
# 根据io操作号，对应io操作对象
dict_filene = {sockfd.fileno(): sockfd}  # 地图搜索功能

# 加入监听
p.register(sockfd, EPOLLIN | EPOLLERR)

while True:
    events = p.poll()  # [(3,1)] 返回元组列表　3为文件号，1为事件号
    for fd, event in events:
        if fd == sockfd.fileno():
            connfd, addr = dict_filene[fd].accept()
            print('Connect from:', addr)
            # 添加监听对象
            p.register(connfd, EPOLLIN | EPOLLHUP)
            # 添加搜索字典
            dict_filene[connfd.fileno()] = connfd
        elif event & EPOLLHUP:  # 连接断开事件符-->POLLHUP
            print('exit')
            p.unregister(fd)
            dict_filene[fd].close()
            del dict_filene[fd]
        elif event & EPOLLIN:  # 读操作事件符-->POLLIN
            data = dict_filene[fd].recv(1024)
            print(data.decode())
            dict_filene[fd].send(b'OK')
