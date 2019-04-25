
from socket import *

s = socket()

s.connect(('0.0.0.0',8800))
f = open('fig.jpg','rb')

while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()