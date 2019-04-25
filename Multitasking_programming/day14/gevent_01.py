import gevent


def foo(a, b):
    print('start %s', a)
    gevent.sleep(1)  # 必须是第三方规定的阻塞
    print('end %s', b)


def bar(a, b):
    print('start %s', a)
    gevent.sleep(5)
    print('end %s', b)


f = gevent.spawn(foo, '!', '!')
b = gevent.spawn(bar, '|', '|')

gevent.joinall([f, b])
