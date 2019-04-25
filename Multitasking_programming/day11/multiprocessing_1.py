'''
multiprocessing　模块
多进程流程：
    1.将需要子进程处理的逻辑封装成函数
    2.通过Process类创建进程对象，然后关联函数
    3.通过进程对象对进程进行属性设置
    4.通过start启动进程
    5.通过jion回收进程
接口使用：
　Process类
'''
import multiprocessing as mp
from time import sleep


def fun():
    sleep(3)
    print('子进程执行事件')


# 创建进程对象
# target 指的是子进程执行的函数
p = mp.Process(target=fun)
# 启动进程
p.start()

# 父进程执行
sleep(2)

# 回收进程
p.join()
print('==================')
