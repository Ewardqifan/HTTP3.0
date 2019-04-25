'''
queue　在内存在建立队列模型，进程通过队列存取消息实现通信
        特点：先进<-->先出
'''

from multiprocessing import Queue
'''
# 创建队列
# maxsize代表最多存放多少个消息
q = Queue(maxsize=0)
# 存入消息
q.put(data, [block, timeout])
# 存入内容data可以是所有数据类型
# block 是否阻塞?　默认为Ture　-->　队列满了还要存，阻塞
# timeout 为超时时间
q.get([block, timeout])
# 从队列中取出消息，参数同上.
# 队列空了还要取，阻塞
# >>先进先出<<
q.full()  # 判断队列是否为满
q.empty()  # 判断队列是否为空
q.qsize()  # 过去队列中消息个数
q.close()  # 关闭队列
'''
