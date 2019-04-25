from multiprocessing import Process
import time


class ClockProcess(Process):
    def __init__(self, value):
        self.value = value
        super().__init__()

    # 重写run方法 --> 可以通过run　方法调用更丰富的方法实现功能
    def run(self):
        for i in range(5):
            print('The time is %s' % time.ctime())
            time.sleep(self.value)


# 创建进程
p = ClockProcess(2)
p.start()
p.join()
