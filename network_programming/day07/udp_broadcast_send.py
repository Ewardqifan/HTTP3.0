from socket import *
from time import sleep

dest = ('176.234.2.255',6666)

data = '''
================
老铁双击666
老铁双击666
老铁双击666
老铁双击666
老铁双击666
老铁双击666
老铁双击666
================
'''

s = socket(AF_INET,SOCK_DGRAM)

# 设置可以接受发送接受广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,True)

while True:
    sleep(2)
    s.sendto(data.encode(),dest)
    print('---')
