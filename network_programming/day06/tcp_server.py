import socket
import time


# 服务端建立过程

# 创建套接字对象
sockfd = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# family IP类型
# type TCP or UDP?
# 绑定地址
sockfd.bind(('0.0.0.0', 8888))

# 设置监听
sockfd.listen(10)
# 传入参数：　监听队列大小

# 等待处理客户端请求
while True:
    print('waiting for connect.....')
    try:
        connfd, addr = sockfd.accept()
    except KeyboardInterrupt:
        print('Server exit')
        break
    print('connect from ', addr)
    # connfd -- 客户点连接套接字 --> 负责交换数据的新的套接字对象 -->　相对的sockfd是为了建立连接
    # addr -- 连接的客户端地址
    # 是一种阻塞函数

    # 收发数据
    # 接收
    while True:

        data = connfd.recv(1024)
        # buffersize 代表每次接受消息的大小
        # 阻塞函数
        # 接受到bytes格式
        if data == b'': # 连接断开后会收到空
            print('connect stop')
            break
        print('Receive message:%s' % (data.decode()))
        # 　发送
        n = connfd.send(b'Receive your message')# 如果连接断开，第一次发送没有异常，但第二次发送会显示broken pipe的异常
        # data要求是bytes格式
        # str --> bytes  string.encode()
        # bytes --> str  bytes.decode()
    connfd.close()


# 关闭套接字
# sockfd.close()
