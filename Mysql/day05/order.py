'''
    订单模型类
'''


class Order():

    def __init__(self, order_id, cust_id, products_num, amt):
        self.order_id = order_id
        self.cust_id = cust_id
        self.products_num = products_num
        self.amt = amt

    def __str__(self):
        str = '订单编号：%s｜客户编号：%s｜产品数量：%d｜订单金额：%.2f' \
              % (self.order_id, self.cust_id, self.products_num, self.amt)

        return str
