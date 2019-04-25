'''
       --> 结构(网络,并发,TCP?UDP?,C与S怎么设计,交流协议?)
功能 --|                                              --> 封装
       --> 技术要点(实现流程的大概框架)

function:
    1.c/s,要求可以多个客户点同时操作
    2.客户端功能,可以查看服务器中有哪些文件(普通文件,不包含隐藏)
    3.客户端可以从服务器下载文件到本地目录下
    4.客户端可以将本地文件上传到客户点
    5.在客户端打印简单的命令提示界面

技术分析(明确结构)
    1.单个服务器长期占用服务器,多个客户端可以同时操作 --> 多进程 --> fork
    2.文件传输 --> 稳定面向连接 --> TCP
    3.查看文件?怎么办? --> 客户端发一个请求,服务器(建立test目录存储文件)将文件名列表发送
        c:
        进入后先打印界面
        选择功能执行功能
        s:
        搭建fork并发网络连接
        使用子进程循环接受请求处理
    4.类与函数并行封装

具体功能模块:

    网络连接
    查看文件
    下载文件
    上传文件
    客户端退出
'''

