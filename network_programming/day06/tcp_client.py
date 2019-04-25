import socket

# 创建套接字对象，注意一定于服务器段的类型相同
sockfd = socket.socket()

#建立连接
server_addr = ('127.0.0.1',8888)
sockfd.connect(server_addr)

#收发消息,先发后收
while True:
    data = input('>>')
    if data == '':
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print('From server:%s'%(data.decode()))

# 关闭套接字
sockfd.close()