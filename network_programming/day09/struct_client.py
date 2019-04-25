from socket import *
import struct

fmt = 'i32sif'
ADDR = ('0.0.0.0',8880)
s = socket()
s.connect(ADDR)

while True:
    print('======')
    id = int(input('ID:'))
    name = input('Name:')
    age = int(input('Age:'))
    score = float(input('Score:'))
    data = struct.pack(fmt,id,name.encode(),age,score)
    s.send(data)
    print('From server:%s'%(s.recv(1024)))
