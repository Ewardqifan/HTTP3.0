'''
    自定义线程类:
        使用自定义线程完成<凉凉>这首歌

'''

from threading import Thread
from time import ctime, sleep

'''
class CustomThread(Thread):
    def __init__(self,args, kwargs):
        super().__init__(args=args, kwargs=kwargs)

    def run(self):
        for i in range(self._args[0]):
            sleep(1)
            print('%s--%s' % (ctime()[11:19], self._kwargs[i]))


kwargs = {0: '凉凉夜色为你思念成河', 1: '化作春泥呵护着我',
          2: '浅浅岁月拂满爱人袖', 3: '片片芳菲入水流'}

ct = CustomThread(args=(4,), kwargs=kwargs)
ct.start()
ct.join()
'''

def player(sec,words):
    for i in range(sec):
        sleep(1)
        print('%s--%s' % (ctime()[11:19], words[i]))

class MyThread(Thread):
    def __init__(self, target, args=(), kwargs={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs
        # super().__init__(target,args,kwargs) 一般不传入父类
    
    def run(self):
        self.target(*self.args,**self.kwargs)


myt2 = MyThread(player,(4,{0: '凉凉夜色为你思念成河', 1: '化作春泥呵护着我',
          2: '浅浅岁月拂满爱人袖', 3: '片片芳菲入水流'}))
myt2.start()
myt2.join()


'''
class MyThread(Thread):

    def __init__(self,target,args=(),kwargs={}):
        super().__init__(target=target,args=args,kwargs=kwargs)


kwargs = {0: '凉凉夜色为你思念成河', 1: '化作春泥呵护着我',
          2: '浅浅岁月拂满爱人袖', 3: '片片芳菲入水流'}
myt1 = MyThread(target=player,kwargs={'sec':4,'words':kwargs})
myt1.start()
myt1.join()
'''