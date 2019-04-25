'''
python　同其他语言的通讯交互可能会使用到
将一组简单的数局转化为二进制格式　或者　将二进制转化为python数据类型
'''
from struct import *

'''
    # Functions
    'calcsize', 'pack', 'pack_into', 'unpack', 'unpack_from',
    'iter_unpack',

    # Classes
    'Struct',

    # Exceptions
    'error'
'''
# help(Struct)
# s = Struct('3si5s')
# data = s.pack(b'No.',10086,b'Eward')
# print(s.unpack(data))

# data = pack('3si5s',b'No.',10086,b'Eward')
# print(unpack('3si5s',data))

'''
从客户端输入学生的id(int),姓名(str),年龄(int),成绩(f)
打包发送给服务端，服务端将其存入一个数据表(表和库都是存在的)
'''
import pymysql
from socket import *

st = Struct('i32sif')
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)

host = '127.0.0.1'  # 'localhost'
user = 'root'
password = '123456'
datebase_name = 'NetWork'

sockfd.bind(('0.0.0.0', 8880))
sockfd.listen(3)

connfd, addr = sockfd.accept()
print('Connect from :', addr)
data = connfd.recv(1024)
print(data)
connfd.send(b'OK')

data = st.unpack(data)
id = data[0]
name = data[1].decode()
age = data[2]
score = data[3]
print(id, name, age, score)


db = pymysql.connect(host, user,
                     password, datebase_name)

cursor = db.cursor()

sql = '''
Insert into studenttest VALUES 
(%d,'%s',%d,%.2f);
''' % (id, name, age, score)

try:
    cursor.execute(sql)
    db.commit()
    print('执行成功')
except Exception as e:
    db.rollback()
    print(e)

cursor.close()
db.close()

connfd.close()
sockfd.close()
