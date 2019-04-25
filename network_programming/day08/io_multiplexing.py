import select  # 用于io多路复用的标准模块
from socket import *

f = open('fig.jpg')
s = socket()
s.bind(('0.0.0.0', 8800))
s.listen(3)

print('IO监控')

rs, ws, xs = select.select([s], [], [f])

print(rs, ws, xs)
