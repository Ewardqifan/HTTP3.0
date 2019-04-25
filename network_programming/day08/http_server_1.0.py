'''
接受浏览器请求
将固定网页发送给浏览器
'''

from socket import *


def handle_request(con_socket):
    print('Request from:', con_socket.getpeername())
    request = con_socket.recv(4096)
    request_lines = request.splitlines()  # 按行分割得到列表
    for line in request_lines:
        print(line)
    try:
        f = open('index.html', 'rb')
    except IOError:
        response = b'HTTP/1.1 404 Not Found\r\n'  # 换行必须要有
        response += b'\r\n'  # 响应头
        response += b'==Sorry not found=='  # 响应体
    else:
        response = b'HTTP/1.1 200 OK\r\n'
        response += b'\r\n'
        response += f.read()
        f.close()
    finally:
        con_socket.send(response)




def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    sockfd.bind(('0.0.0.0', 8000))
    sockfd.listen(5)
    print('Listen the port 8000...')
    while True:
        connfd, addr = sockfd.accept()
        print('connect into :', addr)
        handle_request(connfd)
        connfd.close()


if __name__ == '__main__':
    main()
