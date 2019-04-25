'''
1.使用multiprocess创建两个子进程,分别复制一个文件的上下两部分到一个新的文件中
文件类型不限(图片,文本,音频,视频,etc....)
2.将聊天室代码周末再写一边(尝试用其他的方法，io多路复用，multiprocess写一边)，周内梳理
3.看看sql语句,pymysql
'''
# os.path.getsize(path)将返回 path 参数中文件的字节数。
import multiprocessing as mp
import os
'''
# 文件路径
PATH = 'fig.jpg'


# PATH = './fig.jpg'
# 获取文件字节大小

def read(seek):
    f = open(PATH, 'rb')
    len = os.path.getsize(PATH)
    if seek == 0:  # 从零开始读
        data = f.read(int(len / 2))
    else:  # 从一半开始读
        f.seek(int(len / 2))
        data = f.read()
    f.close()
    return data


def save(seek, path):
    data = read(seek)
    f = open(path, 'wb')
    f.write(data)
    f.close()


process = []
for i in range(2):
    p = mp.Process(target=save, args=(i, 'new_fig_%s.jpg' % i))
    process.append(p)
    p.start()

for j in process:
    j.join()
   
'''
# ============================================

PATH = './fig.jpg'
size = os.path.getsize(PATH)


def top():
    f = open(PATH, 'rb')
    n = size // 2
    with open('top.jpg', 'wb') as fw:
        fw.write(f.read(n))
    f.close()


def bottom():
    f = open(PATH, 'rb')
    with open('bottom.jpg', 'wb') as fw:
        fw.seek(size // 2, 0)  # 移动文件指针　代表从0开始，移动size // 2
        fw.write(f.read())
    f.close()

p1 = mp.Process(target=top)
p2 = mp.Process(target=bottom)
p1.start()
p2.start()
p1.join()
p2.join()