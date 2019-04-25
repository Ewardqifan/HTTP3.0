'''
Chat room server
env:python3.5
exc:for socket and fork
'''
import os
from socket import *
import sys

ADDR = ('127.0.0.1', 8888)


def udp_client():
    '''
        创建客户端套接字
    :return: 返回套接字对象
    '''
    return socket(AF_INET, SOCK_DGRAM)


def login(sockfd):
    '''
        登录网络聊天室
    :param sockfd:udp网络连接套接字对象
    :return: None
    '''
    while True:
        name = input('name:')
        msg = 'L ' + name  # L表示请求类型，为登录消息
        sockfd.sendto(msg.encode(), ADDR)
        data, addr = sockfd.recvfrom(1024)
        print(data.decode())
        if data.decode() == 'OK':
            break
    return name


def chat(sockfd, name):
    '''
        向服务器发送消息,两个进程一收一发
    :param sockfd: udp连接套接字
    :return: None
    '''
    pid = os.fork()
    if pid < 0:
        print('\n==subprocess error==')
    elif pid == 0:
        # 子进程,发;子进程不会结束
        # 下面的可以封装到一个函数中
        while True:
            try:
                msg = input('>>')
            except:
                msg = 'quit'
            if msg.strip() == 'quit':  # 删去两边的空格
                exit_chat(sockfd)  # 退出聊天室
            else:
                msg = 'M ' + name + ' ' + msg
                try:
                    sockfd.sendto(msg.encode(), ADDR)
                except:
                    print('\n==fail to send==')
    else:
        # 父进程,收;父进程也不会结束
        # 下面的可以封装到一个函数中
        while True:
            data, addr = sockfd.recvfrom(1024)
            print(data.decode()+'\n>>',end='')
            if data.decode() == '----Confirm the exit----':
                sys.exit()


def exit_chat(sockfd):
    sockfd.sendto(b'E', ADDR)
    print('\n==Success exit==')
    sys.exit('退出聊天室')


if __name__ == '__main__':
    s = udp_client()
    name = login(s)
    chat(s, name)
