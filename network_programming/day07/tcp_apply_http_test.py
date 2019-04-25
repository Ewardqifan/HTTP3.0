from socket import *

# HTTP 数据传输是一个 TCP 传输的应用

s = socket(AF_INET, SOCK_STREAM)
s.bind(('0.0.0.0', 8000))
s.listen(5)
c, addr = s.accept()
print('ADD:', addr)
data = c.recv(4096)

c.send(b'hellow world')
print(data)

c.close()
s.close()
