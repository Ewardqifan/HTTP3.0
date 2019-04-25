'''
    处理逻辑操作没有sql语句
'''
from order_dao import *
from order import *

class OrderManage():

    def __init__(self):
        self.order_dao = OrderDAO()

    def query_all_order(self):
        '''
            返回订单对象列表
        :return:
        '''
        return self.order_dao.query_all_order()

    def query_by_id(self,id):

        return self.order_dao.query_by_id(id)

