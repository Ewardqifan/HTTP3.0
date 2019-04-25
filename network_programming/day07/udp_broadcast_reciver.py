from socket import *

s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_BROADCAST, True)

s.bind(('0.0.0.0', 6666))  # 接收自己的端口

while True:
    msg, addr = s.recvfrom(1024)
    print(msg.decode())
