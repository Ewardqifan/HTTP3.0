from socket import *
import os, sys, signal, time

HOST = '0.0.0.0'
PORT = 8889
ADDR = (HOST, PORT)
FILE_PATH = '/home/tarena/1902_edward/month02/Multitasking_programming/day13/test/'
print(FILE_PATH)
print(os.listdir(FILE_PATH))


class FtpServer():
    '''
        处理请求功能类:封装不同的方法处理不同的请求类型
            主体思想:接受请求内容后发送准备就绪消息,然后再处理相应操作,类似与TCP握手协议
    '''

    def __init__(self, c):
        self.c = c

    def do_list(self):
        '''
            处理查看文件请求
        :return:
        '''
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.c.send(b'empty')
            return
        else:
            self.c.send(b'OK')
        files = ''
        for i in file_list:
            if i[0] != '.' and os.path.isfile(FILE_PATH + i):
                files += i + '#'  # 人为制造消息边界
                print(files)
        self.c.send(files.encode())

    def do_get(self, filename):
        '''
            处理下载文件请求
        :param filename: 要下载的文件名称
        :return:
        '''
        try:  # 判断文件是否存在
            f = open(FILE_PATH + filename, 'rb')
        except IOError:
            self.c.send('文件不存在'.encode())
            return
        else:
            self.c.send(b'OK')
            time.sleep(0.1)
        while True:  # 循环读取发送
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.c.send(b'##')
                break
            self.c.send(data)
        f.close()

    def do_upload(self, filename):
        '''
            上传文件
        :param filename: 要上传的文件名称
        :return:
        '''
        if os.path.isfile(FILE_PATH + filename):  # 判断服务器中是否有同名文件
            self.c.send('文件已经存在'.encode())
            return
        else:
            self.c.send(b'OK')
            time.sleep(0.1)
        with open(FILE_PATH + filename, 'wb') as f:
            while True:  # 循环写入流程,为什么这里没有清零?
                data = self.c.recv(1024)
                if data == b'##':
                    break
                f.write(data)


def do_request(c):
    '''
        处理请求主函数:判断请求类型,分别交给相应的函数处理
    :param c: 客户端连接套接字
    :return: 无
    '''
    ftp = FtpServer(c)
    while True:
        data = c.recv(4096).decode()
        print(data)
        if not data or data[0] == 'Q':
            c.close()
            return
        # 处理请求
        elif data[0] == 'L':
            # 查看服务端文件列表
            ftp.do_list()
        elif data[0] == 'U':
            data = data.split(' ')
            #  上传文件
            ftp.do_upload(data[1])
        elif data[0] == 'D':
            #  下载文件
            data = data.split(' ')
            ftp.do_get(data[1])


def s_connect():
    '''
        主程序,建立TCP套接字服务器
        循环监听是否有接入
        如果有接入创建子进程处理请求
        将所有的连接关闭放在这里
    :return:
    '''
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    s.bind(ADDR)
    s.listen(5)
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print('Listen the port 8889...')
    # 循环等待客户端连接
    while True:
        try:
            c, addr = s.accept()
        except KeyboardInterrupt:
            sys.exit('exit')
        except Exception as e:
            print(e)
            continue
        print('Connect from', addr)
        pid = os.fork()
        if pid == 0:  # 子进程
            s.close()  # 关闭子进程套接字不影响父进程
            do_request(c)
            os._exit(0)
        else:
            c.close()


if __name__ == '__main__':
    s_connect()
