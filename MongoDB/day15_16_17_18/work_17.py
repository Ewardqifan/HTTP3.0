'''
    自己学习3个聚合操作符的使用
    银行 修改 删除 练习
    复习聊天室,ftp,httpserver2.0
'''

# 自学三个聚合操作符
# $stdDevPop, 返回所有聚合文档中某个域的标准差
# 下面的例子说的是,先通过name域聚合,在返回各个聚合项中age域的标准差.当所求标准差域的数据类型不是数字是返回null
# db.class2.aggregate({$group:{_id:'$name',dev:{$stdDevPop:'$age'}}})
# db.class0.aggregate({$group:{_id:'$gender',dev:{$stdDevPop:'$age'}}})




# $floor,下取整
# db.sales.aggregate({$project:{_id:0}})
# db.sales.aggregate({$project:{_id:0,quantity:{$floor:'$quantity.2019Q1'}}})



# $filter,{ $filter: { input: <array>, as: <string>, cond: <expression> } }
# 数组判断是否存在满足某个条件的值
# 参数1:需要判断的数组 2.数字的重命名(在cond中使用) 3.条件表达式
#     这里的条件表达式和find中的有很大不同
# 下面说的是,显示name,rank,score数组中存在大于90的文档
# in:db.class1.aggregate({
#                      $project:
#                               {name:1,rank:1,_id:0,score:{
#                                                           $filter:{
#                                                                   input:'$score',as:'score',cond:{$$gte:['$score',90]}
#                                                                   }
#                                                           }
#                               }
#                      })
#
# out:{ "name" : "q", "rank" : "A", "score" : [ ] }
#     { "name" : "w", "rank" : "A", "score" : [ 851 ] }
#     { "name" : "e", "rank" : "B", "score" : [ ] }
#     { "name" : "r", "rank" : "D", "score" : [ ] }



