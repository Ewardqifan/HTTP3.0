# 通过一种特定的套接字文件在内存中形成，本机进程间的数据交换
from socket import *
import os

# 本地套接字文件 一次性文件
sock_file = './sock'
if os.path.exists(sock_file):
    os.remove(sock_file)
# 创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)
# 绑定本地套接字
sockfd.bind(sock_file)
sockfd.listen(3)
while True:
    c,addr = sockfd.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
    c.close()

sockfd.close()

