import random


def i_s(value):
    for i in range(1, len(value)):
        # 确定插入数据的索引
        temp = value[i]
        pos = i
        for j in range(i - 1, -1, -1):
            # 从后往前扫描所有有序数据
            if temp >= value[j]:
                pos = j + 1
                break
            else:
                value[j + 1] = value[j]
                pos = j
        value[pos] = temp


def q_s(value):
    # 递归的退出条件:分组排序后前后都剩1

    # 仅有一个数据时候退出
    if len(value) < 2:
        return value
    mark = value[0]
    smaller = [x for x in value if x < mark]
    bigger = [x for x in value if x > mark]
    eq = [x for x in value if x == mark]
    return q_s(smaller) + eq + q_s(bigger)


if __name__ == '__main__':
    list_value = [random.randint(0, 100) for i in range(10)]
    print(list_value)

    q_s(list_value)
    # i_s(list_value)
    print(list_value)
