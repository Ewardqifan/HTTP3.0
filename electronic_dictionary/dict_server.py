'''
    电子词典服务端
'''

from socket import *
import pymysql
import os, sys
import time
import signal

# 1.全局变量
if len(sys.argv) < 3:
    print('Run server as : python3 dict_server.py 0.0.0.0 8000')
    sys.exit()

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
DICT_TEXT = './dict.txt'


# 2.搭建网络连接 : 连接数据库 --> 创建套接字 --> 处理僵尸进程 --> 循环模型等待连接 --> 连接后创建子进程
def main():
    # 连接数据
    db = pymysql.connect('localhost', 'root', '123456', 'dict')
    # TCP创建套接字
    s = socket()
    # 设置端口复用选项
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)

    # 处理僵尸进程
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)

    # 循环等待客户端连接
    while True:
        try:
            c, addr = s.accept()
            print('Connect from :', addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit()  # 服务器退出
        except Exception as e:
            print(e)
            continue

        # 创建子进程
        pid = os.fork()
        if pid == 0:  # 子进程
            s.close()
            db_request(c, db)
            sys.exit()
        else:
            c.close()


# 3.处理请求逻辑处理部分
def db_request(connfd, db):
    while True:
        date = connfd.recv(1024).decode()
        print(connfd.getpeername(), ':', date)
        if date[0] == 'R':
            do_register(date, connfd, db)


def do_register(date, c, db):
    tmp = date.split(' ')
    name = tmp[1]
    passwd = tmp[2]
    cursor = db.cursor()

    sql = "select * from user WHERE name='%s'" % name
    cursor.execute(sql)
    result = cursor.fetchone()
    if result != None:
        c.send('该用户以存在'.encode())
        return
    sql = "insert into user(name, passwd) VALUES ('%s','%s')" % (name, passwd)
    try:
        cursor.execute(sql)
        db.commit()
        c.send(b'OK')
    except:
        db.rollback()
        c.send('注册失败'.encode())


if __name__ == '__main__':
    main()
