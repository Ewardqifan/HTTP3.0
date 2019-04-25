# 使用TCP 完成一个文件的输出，
# 要求客户点发送给服务端
# 文件类型可以是图片或者文本－－不限
# tcp 与　udp　的基础代码

from socket import *

s = socket()
s.bind(('0.0.0.0', 8800))
s.listen(5)

c, addr = s.accept()
print('ADD:', addr)

f = open('work_recv.jpg', 'wb')
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

print('meg has recivered')

c.send(b'OK')
f.close()
c.close()
s.close()
