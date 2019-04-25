from socket import *
import sys, os, time

ADDR = ('0.0.0.0', 8889)


class FtpClient():
    def __init__(self, s):
        self.s = s

    def do_list(self):
        self.s.send(b'L')  # 发送请求
        data = self.s.recv(1024).decode()
        print(data)
        if data == 'OK':  # 服务端同意发送
            file = self.s.recv(4096).decode()
            for i in file.split('#'):
                print(i)
        else:
            print(data)

    def do_quit(self):
        self.s.send(b'Q')
        self.s.close()
        sys.exit('谢谢使用')

    def do_get(self, filename):
        self.s.send(('D ' + filename).encode())
        data = self.s.recv(128).decode()
        if data == 'OK':
            with open(filename, 'wb') as f:
                while True:
                    data = self.s.recv(1024)
                    if data == b'##':
                        break
                    f.write(data)
        else:
            print(data)

    def do_upload(self, filename):
        self.s.send(('U ' + filename).encode())
        data = self.s.recv(128).decode()
        if data == 'OK':
            try:
                f = open(filename, 'rb')
            except IOError:
                print('文件不存在')
                return
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.s.send(b'##')
                    break
                self.s.send(data)
            f.close()
        else:
            print('文件已经存在')


def main():
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return

    # 功能对象,用于客户端实现发送请求的功能
    ftp = FtpClient(s)

    while True:
        print('================')
        print('***   Look   ***')
        print('*** Download ***')
        print('***  Upload  ***')
        print('***   Quit   ***')
        print('================')

        cmd = input('>>')
        if cmd.strip() == 'Look':
            ftp.do_list()
        elif cmd.strip() == 'Quit':
            ftp.do_quit()
        elif cmd.strip() == 'Download':
            filename = input('请输入文件名:')
            filename = filename.strip()
            ftp.do_get(filename)
        elif cmd.strip() == 'Upload':
            filename = input('请输入文件名:')
            filename = filename.strip()
            ftp.do_upload(filename)
        else:
            print('请输入正确命令')


if __name__ == '__main__':
    main()
