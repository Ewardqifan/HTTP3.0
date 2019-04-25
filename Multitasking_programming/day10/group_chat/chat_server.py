'''
Chat room server
env:python3.5
exc:for socket and fork
'''
import os
from socket import *

# 服务端网络地址
ADDR = ('127.0.0.1', 8888)
# 存储用户
USER = {}


# 搭建网络连接
def udp_server():
    '''
        创建服务端套接字
    :return: 套接字对象
    '''
    sockfd = socket(AF_INET, SOCK_DGRAM)
    sockfd.bind(ADDR)
    return sockfd


def do_login(sockfd, name, addr):
    '''
        判断是否加入，通知其他用户
    :param sockfd: upd连接套接字对象
    :param name: 用户姓名
    :param addr: 用户地址
    :return: None
    '''
    if (name in USER) or ('Administrator' in name):
        sockfd.sendto(b'----User Exist----', addr)
        return
    USER[name] = addr
    sockfd.sendto(b'OK', addr)
    # 通知其他人
    msg = '----welcome %s come in the room----' % (name)
    for i in USER:
        sockfd.sendto(msg.encode(), USER[i])
    # 加入用户字典


def do_msg(sockfd, msg, addr,name):
    '''
        向其他用户发送消息
    :param sockfd: udp连接套接字
    :param msg: 收到的消息
    :param addr: 收到消息的地址
    :return: None
    '''
    msg = name + ': ' + msg
    for i in USER:
        if USER[i] == addr:
            sockfd.sendto(b'\n----send successfully----', USER[i])
        else:
            sockfd.sendto(msg.encode(), USER[i])


def do_exit(sockfd, addr):
    '''
        从用户字典中删除退出用户
        退出发送信息给其他用户
    :param sockfd: udp连接套接字
    :param addr: 退出用户的地址
    :return: None
    '''
    sockfd.sendto(b'\n----Confirm the exit----', addr)
    name = None
    for n, a in list(USER.items()):  # 字典在遍历的时候无法更改，先转换为列表形式
        if a == addr:
            name = n
            del USER[n]
    msg = '\n----%s has exited----' % (name)
    for i in USER:
        sockfd.sendto(msg.encode(), USER[i])


def request(sockfd):
    '''
        处理客户端请求
    :param sockfd:udp连接套接字
    :return: None
    '''
    while True:
        data, addr = sockfd.recvfrom(1024)
        msgList = data.decode().split(' ')
        if msgList[0] == 'L':
            do_login(sockfd, msgList[1], addr)
        elif msgList[0] == 'M':
            name = msgList[1]
            msgList = ' '.join(msgList[2:])
            do_msg(sockfd, msgList, addr, name)
        elif msgList[0] == 'E':
            do_exit(sockfd, addr)


if __name__ == '__main__':
    s = udp_server()
    pid = os.fork()
    if pid<0:
        pass
    if pid == 0:
        msg = input('>>')
        msg = 'M Administrator ' + msg
        s.sendto(msg.encode(),ADDR)
    else:
        request(s)
