'''
    共享内存：
        在内存中开辟一块空间，进程可以写入和读取内容，但是每次写入内容会覆盖之前的内容
        很简单暴力但是很快
'''
'''
from multiprocessing import Value, Array
# 创建共享内存
obj = Value(ctype, data)
# ctype -->共享内存类型{c i f 字符(！单个字符，不是字符串！) 整形 浮点型}
# data --> 共享内存初始数据
# obj.value 对该属性修改查看即就是共享内存的读写
'''

from multiprocessing import Process, Value, Array
import time
import random

#
# # 创建共享内存
# money = Value('i', 5000)
#
#
# # 操作共享内存
# def man():
#     for i in range(30):
#         time.sleep(0.2)
#         money.value += random.randint(1, 1000)
#
#
# def girl():
#     for i in range(30):
#         time.sleep(0.18)
#         money.value -= random.randint(100, 800)
#
#
# th = [man, girl]
# process = []
# for i in th:
#     p = Process(target=i)
#     p.start()
#     process.append(p)
#
# for i in process:
#     i.join()
#
# print('余额：', money.value)

'''
obj = Array(ctype,data)
ctype -->　共享内存类型
data -->　列表表示共享内存初始数局
        　整数表示共享内存开辟的数据元素个数
通过索引和遍历的方式获取值
'''

# # 创建共享内存
# # shm = Array('i', [1, 2, 3, 4]) # -->[1,2,3,4]
# shm = Array('i', 5) # --> [0,0,0,0,0]
#
#
# def fun():
#     for i in shm:
#         print(i,end=',')
#     shm[1] = 200
#
# p = Process(target=fun)
# p.start()
# p.join()
#
# print()
# for i in shm:
#     print(i,end=',')


shm = Array('c', b'Hello')  # -->[H,e,l,l,o]
print(shm.value)  # 专门打印字节串
