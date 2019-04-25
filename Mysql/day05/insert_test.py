import pymysql
from db_conf import *

# 连接数据库
conn = pymysql.connect(host, user,
                       password, datebase_name)

cursor = conn.cursor()

# sql = """
# insert into orders(order_id,cust_id)
# VALUES ('201001010007','C00000007');
# """
# sql = '''
# delete from orders
# WHERE order_id = '201201010007';
# '''
sql = '''
update orders set order_id = NULL 
WHERE cust_id = 'C00000001'
'''

cursor.execute(sql)
conn.commit()
print('执行成功')
cursor.close()
conn.close()