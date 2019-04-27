'''
 电子词典客户端
'''

from socket import *
import sys
import getpass


def main():
    ADDR = ('176.234.2.91', 8000)
    s = socket()
    try:
        s.connect(ADDR)
    except Exception as e:
        print(e)
        return

    while True:  # 一级界面
        print('''
                 1.注册
                 2.登录
                 3.退出
        ''')
        cmd = input('输入选项:')
        s.send(cmd.encode())
        if cmd not in ['1', '2', '3']:
            print('请输入正确选项')
            continue
        elif cmd == '1':
            do_register(s)
        elif cmd == '2':
            pass
        elif cmd == '3':
            pass


def do_register(s):

    while True:
        name = input('请输入账号:')
        password = getpass.getpass('Password:')
        if (' ' in name) or (' ' in password):
            print('用户名或密码中不能有空格')
            continue
        re_password = getpass.getpass('请确认密码:')
        if password != re_password:
            print('不一致,重新输入')
            continue
        print('账号名称:', name)
        print('密码:', password)

        msg = 'R' + ' ' + name + ' ' + password
        s.send(msg.encode())
        server_msg_name = s.recv(1024).decode()
        if server_msg_name == 'OK':
            print('注册成功')
            return
        else:
            print(server_msg_name)



if __name__ == '__main__':
    main()
