from socket import *
import sys
from threading import Thread
from config import *
import re
import json  # 解析json文件

ADDR = (HOST, PORT)


# 负责和web frame 通信
# 我们规定httpserver与webframe的数据交互模式:
#    http --> web  {method:'GET',info:'请求内容'}
#    web --> http  {status:'200',data:'逻辑处理后的内容'}
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip, frame_port))  # 连接webframe
    except Exception as e:
        print(e)
        return
    else:
        env = json.dumps(env).encode()
        s.send(env)
        # 接收json文件
        data = s.recv(4096 * 100).decode()
        return json.loads(data)


class HTTPServer(object):
    def __init__(self, addr):
        self.addr = addr
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, REUSE_PORT)

    def bind(self):
        self.sockfd.bind(self.addr)
        self.ip = self.addr[0]
        self.port = self.addr[1]

    def server_forever(self):
        self.sockfd.listen(5)
        print('Listen the port %d...' % self.port)
        while True:
            connfd, addr = self.sockfd.accept()
            print('Connect from', addr)
            client = Thread(target=self._handle, args=(connfd,))
            client.setDaemon(True)
            client.start()

    def _handle(self, connfd):
        request = connfd.recv(1024).decode()
        # print(request)
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'  # 正则表达
        try:
            env = re.match(pattern, request).groupdict()
            print(env)  # 按捕获组生成对象字典
        except:
            connfd.close()
            return
        else:
            data = connect_frame(env)  # 连接webframe data str.
            if data:
                self.response(connfd, data)  # data 为None

    def response(self, connfd, data):  # 将数据发送给浏览器
        if data['status'] == '200':
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
        elif data['status'] == '404':
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']
        elif data['status'] == '500':
            pass
        else:
            pass
        # 将数据发送给浏览器
        response_data = responseHeaders + responseBody
        # print(response_data)
        connfd.send(response_data.encode())


if __name__ == '__main__':
    httpd = HTTPServer(ADDR)
    try:
        httpd.server_forever()
    except KeyboardInterrupt:
        print('退出')
    except Exception as e:
        print(e)
