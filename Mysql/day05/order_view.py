'''
    视图层｜用户接口层
'''
from order_manage import *
from order import *

ordermanage = None


def print_menu():
    menu = '''==========订单管理程序==========
             1 - 查询所有订单号             
             2 - 根据ID查询订单             
             3 - 新增订单
             4 - 修改订单
             5 - 删除订单
             其他 - 退出
             =============================='''
    print(menu)

def query_all():

    order_list = ordermanage.query_all_order()
    for row in order_list:
        print(row)

def query_order_by_id(id):

    order = ordermanage.query_by_id(id)

    print(order)






if __name__ == '__main__':
    global ordermanage
    ordermanage = OrderManage()
    while True:
        print_menu()
        oper = int(input('操作序号：'))
        if oper == 1:
            query_all()
        elif oper == 2:
            order_id = input('请输入订单ID:')
            query_order_by_id(order_id)
        elif oper == 3:
            pass
        elif oper == 4:
            pass
        elif oper == 5:
            pass
        else:
            break
