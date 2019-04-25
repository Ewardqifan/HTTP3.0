'''
    设计一个http服务器类,提供给用户

    function:
        1.接受客户端请求
        2.解析客户端请求
        3.根据请求组织数据
        4.将数据以响应格式发送给浏览器

    采用多线程并发,可以满足多客户端同时请求
    网页请求解析
    类封装,将类提供给用户使用

    使用tcp套接字进行数据传输
    使用多线程并发模型
    http协议格式

    使用者想用http这个类干什么?启动服务,用于展示静态网页
    什么需要用户提供?服务端地址和网页
    用户怎样用这个类?
'''

from socket import *
from threading import Thread
import sys


# 封装HTTP类作为一个完整的服务功能
class HTTPServer():
    def __init__(self, server_addr, statis_dir):
        self.addr = server_addr
        self.dir = statis_dir
        # 构建实例对象时就调用函数
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.socket = socket()
        self.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

    def bind(self):
        self.socket.bind(self.addr)
        self.ip = self.addr[0]
        self.port = self.addr[1]

    # 启动服务
    def server_forever(self):
        self.socket.listen(5)
        print('Listen the port %s' % self.port)
        while True:
            try:
                connfd, addr = self.socket.accept()
            except KeyboardInterrupt:
                self.socket.close()
                sys.exit('退出服务器')
            except Exception as e:
                print(e)
                continue
            # 创建分支线程处理请求
            th = Thread(target=self._handle, args=(connfd,))
            th.start()
            th.join()

    def _handle(self, connfd):
        # 接受HTTP请求
        request = connfd.recv(4096)
        # 防止异常断开.客户端突然关闭,向下执行会报错
        if not request:
            return
            # 解析请求
        requestHeaders = request.splitlines()
        print(connfd.getpeername(), ':', requestHeaders[0])
        # 获取请求行,内容
        getRequest = str(requestHeaders[0]).split(' ')[1]
        print(getRequest)
        if getRequest == '/' or getRequest[-5:] == '.html':
            self._get_html(connfd, getRequest)
        else:
            self._get_data(connfd, getRequest)

    def _get_html(self, connfd, getRequest):
        if getRequest == '/':
            filename = self.dir + '/index.html'
        else:
            filename = self.dir + getRequest
        try:
            f = open(filename)
        except IOError:
            # 没有此网页
            responseHeaders = 'HTTP/1.1 404 Not Found\r\n'
            responseHeaders += '\r\n'
            responseBody = 'Sorry, Not found the page'
        else:
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders += '\r\n'
            responseBody = f.read()
            response = responseHeaders + responseBody
        finally:
            connfd.send(response.encode())
            f.close()

    def _get_data(self, c, r):
        data = '''HTTP/1.1 200 OK
        
        <p>Waiting httpserver v3.0</p>
        '''
        c.send(data.encode())


if __name__ == '__main__':
    server_addr = ('0.0.0.0', 8000)
    statis_dir = './static'
    httpd = HTTPServer(server_addr, statis_dir)
    httpd.server_forever()
