'''
    排序算法
        冒泡
        重复走访需要排序的数据,依次对比每两个相邻的元素,如果次序错误则交换
        重复进行直到没有相邻数据需要交换为止,此时完成排序
        每次对比n-1-->n-2-->n-3-->n-4....
        总共对比(n-1)!次
'''
import time
import random
from day15.search import cal_time


def b_s(value):
    for i in range(len(value) - 1):
        flag = False
        for j in range(len(value) - 1 - i):
            if value[j] > value[j + 1]:
                # 数据交换的写法
                value[j], value[j + 1] = value[j + 1], value[j]
                # 若在一次遍历中,数据发生交换则为Ture
                flag = True
        # 当走访一边后发现都没有进行数据交换,则不在遍历数据进行走访交换
        if flag is False:
            break


if __name__ == '__main__':
    heigh = [random.randint(100, 155) for i in range(10)]
    print(heigh)
    b_s(heigh)
    print(heigh)
