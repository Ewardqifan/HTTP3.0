'''
    socketserver 封装后的网络并发编程标准库模块
    使用方法:
        1.创建服务器类,通过选择继承的类决定创建tcp or udp 进程或线程的并发
        2.创建请求处理类,根据服务器类型选择stream or Datagram, 重现handle方法做具体请求处理
        3.通过服务器实例化对象,并绑定请求处理类
        4.通过服务器对象启动服务
'''

from socketserver import *


# 创建tcp多进程并发
class Server(ForkingMixIn, TCPServer):
    pass


# 创建具体的请求处理类
class Handler(StreamRequestHandler):
    def handle(self):
        # 重写处理方法
        print('Connect from:', self.client_address)
        while True:
            # self.request ==> accept->connfd 相当于客户端连接套接字对象
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'OK')


# 创建服务器对象
ser = Server(('0.0.0.0', 8888), Handler)
# 启动服务
ser.serve_forever()
