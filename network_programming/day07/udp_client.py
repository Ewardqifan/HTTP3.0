from socket import *

# 服务端地址变成全局变量
HOST = '176.234.2.85'
PORT = 8888
ADDR = (HOST,PORT)

# 创建数据报套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#先发后收

while True:
    data = input('>>').encode()
    if not data:
        print('键入为空,断开连接')
        break
    sockfd.sendto(data,ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print('From server:',msg.decode())

sockfd.close()

