from socket import *

# 创建数据报套接字
sockfd = socket(AF_INET, SOCK_DGRAM)
# 绑定地址
sockfd.bind(('176.234.2.91', 8888))

while True:
    try:
        # 收发消息
        # 先收
        print('waiting meaasge')
        data, addr = sockfd.recvfrom(1024)
    except KeyboardInterrupt:
        print('取消接受')
        break
    print('Receive from %s:%s'%(addr,data.decode()))
    # 后发
    sockfd.sendto(b'hello brother',addr)

# 关闭套接字对象
sockfd.close()
