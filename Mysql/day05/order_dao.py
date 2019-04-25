# 　订单数据访问对象
# d:data a:access o:object
# 拼装各种sql语句，调用db_helper

from db_helper import DBHelper
from order import Order


class OrderDAO():
    def __init__(self):
        self.db_helper = DBHelper()
        self.db_helper.open_conn()

    def __del__(self):
        self.db_helper.close_conn()

    def query_all_order(self):
        '''
            查询所有订单
        :return: 所有订单实体组成的列表(list) or None
        '''
        order_list = []
        sql = 'SELECT * FROM orders LIMIT 0,10'
        result = self.db_helper.do_query(sql)
        if not result:
            print('查询结果为空')
            return None

        for row in result:
            order_id = row[0]
            cust_id = row[1]
            if row[4]:
                products_num = int(row[4])
            else:
                products_num = 0
            if row[5]:
                amt = float(row[5])
            else:
                amt = 0
            order_list.append(Order(order_id, cust_id, products_num, amt))

        return order_list

    def query_by_id(self, id):

        sql = 'select * from orders WHERE order_id = %s' % (id)
        result = self.db_helper.do_query(sql)[0]
        if not result:
            print('查询结果为空')
            return None
        order_id = result[0]
        cust_id = result[1]
        if result[4]:
            products_num = int(result[4])
        else:
            products_num = 0
        if result[5]:
            amt = float(result[5])
        else:
            amt = 0
        order = Order(order_id, cust_id, products_num, amt)
        return order


if __name__ == '__main__':
    order_dao = OrderDAO()
    order_list = order_dao.query_all_order()
    for order in order_list:
        print(order)
