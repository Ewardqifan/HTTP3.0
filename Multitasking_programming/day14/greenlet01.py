'''
    协程
'''
from greenlet import greenlet


def test1(a):
    print('start 1')
    gr2.switch(2)
    print('end 1')
    gr2.switch()


def test2(b):
    print('start 2')
    gr1.switch()
    print('end 2')


# 将函数变为协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch(1)  # 传参 与 了解
