'''
 通过pymongp
from pymongo import MongoClient

# 1.连接数据库
conn = MongoClient('localhost', 27017)

# 2.选择数据库和集合
db = conn.stu
myset = db.class0

# 3.通过集合对象调用借口完成数据操作:
    数据转换:
    文档 --> 字典
    数组 --> 列表
    布尔 --> python布尔
    null --> None
    操作符 --> 字符串形式原样书写 e.g. $lt --> '$lt'
    操作函数:
    insert_one()
    insert_many()
    cursor = find(query,field) 返回查找结果的游标对象(可迭代对象,由多个字典组成)
                可以使用limit,count,skip,sort.sort-->{x:a,y:b...}-->[(x,a),(y,b),...](a,b=1,-1)
             find_one() 返回文档字典

    update_one()
    update_many()
    update()

    delete_one()
    delete_many()
    remove()

    create_index(index,**kwargs) 创建索引 {name:1} --> [('name',1)] 返回索引名 关键字选项确定唯一索引等选型
    list_indexes() 查看索引
    drop_index() 删除索引
    drop_indexes() 删除所有索引

    aggregate([{},{}....]) 聚合操作 返回可迭代游标对象(类似于find)

# 4.关闭数据库连接
conn.close()
'''

import pymongo

conn = pymongo.MongoClient('localhost', 27017)

db = conn.stu
# myset = db.class4

# myset.insert_one({'name':'张铁林','King':'乾隆'})
# myset.insert_many([{'name':'陈道明','King':'康熙'},{'name':'张国立','King':'康熙'}])
# myset.insert({'name':'唐国强','King':'雍正'})
# myset.insert({'name':'陈建斌','King':'雍正'},{'name':'聂远','King':'乾隆'})
# myset.save({'_id':1,'name':'吴奇隆','King':'四爷'})
# myset.save({'_id':1,'name':'郑少秋','King':'乾隆'})
# =======================================================================
# cursor = myset.find({'name':{'$lt':'唐国强'}}, {'_id': 0})
# for i in cursor:  # i是一个字典数据类型
#     print(i)

# in:   cursor = myset.find({},{'_id':0})
#       for i in cursor.skip(1).limit(3):
#           print(i)
# out:  {'King': '康熙', 'name': '陈道明'}
#       {'King': '康熙', 'name': '张国立'}
#       {'King': '雍正', 'name': '唐国强'}

# cursor = myset.find({},{'_id':0}).sort([('King',1)])
# for i in cursor:
#     print(i)

# file = myset.find_one({'King':'康熙'},{'_id':0})
# print(file)
# ===============================================================
# myset.update_one({'King':'康熙'},{'$set':{'king_name':'玄烨'}})
# myset.update_many({'King':'康熙'},{'$set':{'king_name':'玄烨'}})
# myset.update_one({'King':'康熙'},{'$unset':{'king_name':''}})
# myset.update_many({'King':'雍正'},{'$set':{'king_name':'胤琛'}})
# myset.update_one({'King': '光绪'}, {'$set': {'king_name': '邓超'}}, upsert=True)
# ================================================================
# myset.delete_one({'King':'乾隆'})
# myset.delete_many({'king_name':None}) = myset.delete_many({'king_name':{'$exists':False}})
# myset.remove({'King':'雍正'},multi=False)

# file = myset.find_one_and_delete({'King':'乾隆'})
# print(file)
# ==================================================================
# index_name = myset.create_index([('name',1)],name='first_index')
# print(index_name)
# for i in myset.list_indexes():
#     print(i)
# myset.drop_index([('name', 1)])
# ====================================================================
myset = db.class0

pipe = [{'$match':{'gender':{'$exists':True}}},
        {'$sort':{'age':1}},
        {'$project':{'_id':0}}]

for i in myset.aggregate(pipe):
    print(i)

# for i in dir(myset): #查询myset的属性与方法
#     print(i)

conn.close()
