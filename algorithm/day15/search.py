'''
    算法:
    顺序查找
    二分查找
    原始数据:[12,10,1,3,5,9,11,6,2,4,8,7,13]
'''
import random
import time


def cal_time(fun):
    def func(*args):
        time_start = time.time()
        a = fun(*args)
        print('耗时:%.5f' % (time.time() - time_start))
        return a

    return func


@cal_time
def linear(value, key):
    for i in value:
        if i == key:
            return i
    else:
        return False


@cal_time
def binarysearch(value, key, left, right):
    '''
        有序二分法查找
    :param value: 查找原列表
    :param key: 查找值
    :param left: 当前查找范围左侧数据对应的下表 left
    :param right: 当前查找范围右侧侧数据对应的下表 right
    :return:
    '''
    # 递归退出条件
    if left > right:
        return False
    # 获取中间元素对应下标
    middle = (left + right) // 2
    # 对比中间数据和待查找值: == > <
    if value[middle] == key:
        return middle
    elif value[middle] > key:
        return binarysearch(value, key, left, middle - 1)
    else:
        return binarysearch(value, key, middle + 1, right)

@cal_time
def bs_loop(value, key):
    left = 0
    right = len(value) - 1
    while left <= right:
        middle = (left + right) // 2
        if value[middle] == key:
            return middle
        elif value[middle] > key:
            right = middle - 1
        elif value[middle] < key:
            left = left + 1
    return False

if __name__ == '__main__':
    list = [i for i in range(1, 600000,random.randint(0,9))]
    print(list)
    middle = bs_loop(list,7)
    print(middle)
    # print(binarysearch(list, 6, 0, len(list) - 1))
    random.seed(42)
    random.shuffle(list)
    # print(list)
    middle = linear(list, 7)
    print(middle)
