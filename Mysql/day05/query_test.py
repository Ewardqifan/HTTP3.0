import pymysql
import random
from db_conf import *



# 连接数据库
conn = pymysql.connect(host, user, password, datebase_name)

# 创建游标对象
cursor = conn.cursor()
sql = 'SELECT * FROM orders LIMIT %d,6'%(random.randint(10000,99999))
cursor.execute(sql)
result = cursor.fetchall()# 取出所有数据
for row in result:
    print('订单编号：%s｜客户编号：%s｜金额：%d'%(row[0],row[1],row[5]))
cursor.close()
conn.close()
