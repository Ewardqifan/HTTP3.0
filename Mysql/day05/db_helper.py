# 封装数据库的基本操作
# 连接数据库、关闭连接、执行查询、执行增删改
from db_conf import *
import pymysql


class DBHelper:
    '''
        封装数据库的基本操作
        连接数据库、关闭连接、执行查询、执行增删改
    '''

    def __init__(self):
        self.__db_conn = None  # 数据库连接对象

    def open_conn(self):
        '''
            连接数据库
        :return: None
        '''
        try:
            self.__db_conn = pymysql.connect(
                host, user, password, datebase_name)
        except Exception as e:
            print('连接数据库错误')
            print(e)
        else:
            print('连接数据库成功')

    def close_conn(self):
        '''
            关闭数据库
        :return:None
        '''

        try:
            self.__db_conn.close()
        except Exception as e:
            print('关闭数据库失败')
            print(e)
        else:
            print('关闭数据成功')

    def do_query(self, sql):
        '''
            执行查询操作
        :param sql: sql语句(str)
        :return: 查询结果(tuple) or None
        '''
        try:
            cursor = self.__db_conn.cursor()  # 获取游标
            cursor.execute(sql)
            # 获取游标查询内容
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print('查询失败')
            print(e)
            return None

    def do_update(self, sql):
        '''
            执行增删改操作
        :param sql: sql语句(str)
        :return: None or 受影响的笔数(int)
        '''
        try:
            cursor = self.__db_conn.cursor()
            result = cursor.execute(sql)
            self.__db_conn.commit()
            cursor.close()
            return result  # 返回受影响的笔数
        except Exception as e:
            print('执行失败')
            print(e)
            return None


# 测试
if __name__ == '__main__':

    dbhelper = DBHelper()
    query_sql = '''select * from orders LIMIT 10086,3'''


    dbhelper.open_conn()
    result = dbhelper.do_query(sql=query_sql)
    for i in result:
        print(i)
    dbhelper.close_conn()


    delete_updata = '''
    delete from orders
      WHERE cust_id = 'c00000011'
    '''
    dbhelper.open_conn()
    result = dbhelper.do_update(sql=delete_updata)
    print('删除笔数：%d'%(result))
    dbhelper.close_conn()