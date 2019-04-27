from socket import *
import json
from setting import *
import select
from urls import *

class Application():
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, REUSE_PORT)
        self.sockfd.bind((frame_ip, frame_port))

    def start(self):
        self.sockfd.listen(5)
        print('Listen the port %d' % frame_port)
        rlist = [self.sockfd]
        wlist = []
        xlist = []
        # select IO多路复用
        while True:
            rs, ws, xs = select.select(rlist, wlist, xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd, addr = r.accept()
                    rlist.append(connfd)
                else:
                    self.handle(r)
                    rlist.remove(r)

    def handle(self, connfd):

        request = connfd.recv(1024).decode()
        request = json.loads(request)
        if request['method'] == 'GET':
            if request['info'] == '/' or request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])
            response = json.dumps(response)
            connfd.send(response.encode())
            connfd.close()
        elif request['method'] == 'POST':
            pass
            # dict = {'status':'200','data':'OK'}
            # connfd.send(json.dumps(dict).encode())

    def get_html(self, info):
        print('recv the info :',info)
        if info == '/':
            filename = STATIC_DIR + '/index.html'
            print('filename',filename)
        else:
            filename = STATIC_DIR + info
        try:
            with open(filename) as f:
                data = f.read()
        except IOError:
            return {'status':'404','data':'bye'}
        else:
            return {'status':'404','data':data}


    def get_data(self, info):
        for url,func in urls:
            if url == info:
                return {'status':'200','data':func()}
        return {'status':'404','data':'sorry....'}


if __name__ == '__main__':
    app = Application()
    app.start()
