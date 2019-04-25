'''
    非关系型数据库mongodb

    terminal commond:
        mongostat -查看数据库运行状态
        mongotop - 查看数据库读写时长
        mongodump - 数据备份
        mongorestore - 恢复

    输入help可以看到基本操作命令
    db.help()：显示数据库操作命令，里面有很多的命令
    db.foo.help()：显示集合操作命令，同样有很多的命令，foo指的是当前数据库下，一个叫foo的集合，并非真正意义上的命令
    show users:显示当前所有用户
    db.dropDatabase()删除db所代表的数据库，当前所在的数据库
    show dbs:显示数据库列表
    show collections：显示当前数据库中的集合（类似关系数据库中的表）
    use <db name>：切换当前数据库，这和MS-SQL里面的意思一样
            use yourDB当创建一个集合(table)的时候会自动创建当前数据库
    db.createCollection('class1') 创建集合
    db.collection.insert('class1') 创建集合
    db.collection.drop() 删除集合
    db.collection.renameCollection(name) 集合重命名

    数据类型:
    整型 int
    浮点型 double
    布尔 boolean true fales
    字符串 srting  utf-8
    ObjectId: 文档中文档类型,查找修改删除时'内部域名.外部域名'
    Null型 null

    设计原则:
    一个集合中的文档可以有不同的域,域的个数也可以不一致
    集合中的文档层次不宜嵌套或多,如果层次过多时候应考虑分为多个集合
    在一个集合中的文档应该尽量表达相同类型的数据内容

    时间函数:
    new Date()时间类型,Date()字符串类型,ISODate()将指定的时间转化为标准时间存入
    ISODate().valueof()获取时间戳,

    数据操作:
    1.插入文档
        db.class0.insertOne( obj, <optional params> ) - insert a document, optional parameters are: w, wtimeout, j
        db.class0.insertMany( [objects], <optional params> )
        db.class0.save()
    2.查找文档
        db.class.find([query],[fields]) - query is an optional query filter. fields is optional set of fields to return.
            e.g. db.class.find( {x:77} , {name:1, x:1} )
        db.collection.findOne() 同上只查找一个
            query: $eq:==  $ne:!=
                   $gt:>   $gte:>=
                   $lt:<   $lte:<=
                   $in:包含 $nin:不包含

                   $and:与
                   $or:或 [{},{}....]
                   $not:非
                   $nor:异或 not (a or b) 所有条件均为假才真-->既不...也不...

                   $all:数组查找中查找包含多项 e.g. $all:[a,b,...]
                   $size:根据数组的元素个数查找 $size无法查找某个数组长度不等于某个数的文档,可以用以下方法:
                            db.class1.findOneAndUpdate({'score.3':{$exists:true}},{$pop:{score:1}})
                            {'score.3':{$exists:true}} --> 查找数组第四个索引上存在的文档!

                   $slice:[fields]command e.g. $slice:[a] 查看前a项
                                               $slice:[a,b] 跳过a项,查看后b项
                   'xxx.a':{} 数组xxx第a+1项的要求

                   $exists 查找域存在的文档
                   $mod 根据除数和余数进行查找
                   $type 根据数据类型筛选
    3.数据操作函数
        db.collectionName.distinct(field) 获取集合中某个域的值范围
            db.class0.distinct( key, query, <optional params> )
            - e.g. db.class0.distinct( 'x' ), optional parameters are: maxTimeMS
        db.collectionName.find().pretty()
            - pretty print each document, possibly over multiple lines
        db.collectionName.find().limit(<n>) 显示前n个
        db.collectionName.find().skip(<n>)  跳过前n个
        db.collectionName.find().count(<applySkipLimit>) 统计查询结果的数量
            ps:by default ignores skip,limit
        db.collectionName.find().sort({...})
            ps:{field:1}-->asce/{field:-1}-->desc
        可以通过序列号的方法直接获取集合中的某个文档

execesice:
        1.db.class.find({},{_id:0})
        2.db.class.find({age:8},{_id:0})
        3.db.class.find({age:{$gt:10}},{_id:0})
        4.db.class.find({age:{$gte:8,$lte:12}},{_id:0})
        5.db.class.find({age:9,hobby:{$in:['painting']},sex:'w'},{_id:0})
        6.db.class.find({$or:[{age:{$lt:8}},{age:{$gt:12}}]},{_id:0})
        7.db.class.find({$or:[{age:9,age:11}]},{_id:0})
        8.db.class.find({hobby:{$size:2}},{_id:0})
        9.db.class.find({hobby:{$in:['computer']}},{_id:0})
        10.db.class.find({hobby:{$all:['painting','dance']}},{_id:0})
        11.db.class.find({hobby:{$size:3}},{_id:0}).count()
        12.db.class.find({},{_id:0}).sort({age:-1})[1]
        13.db.class.find({sex:'w'},{_id:0}).sort({age:1}).limit(3)

    4.修改操作
        db.class.updateOne( filter, update, <optional params> )
        db.class.updateMany(filter,update,upsert)
        - update the first matching document, optional parameters are: upsert, w, wtimeout, j
        - filter 筛选条件 同 find
        - update 要修改的数据,同修改操作符一起使用 键值对文档
        - upsert 如果没有query到文档,是否插入新文档 布尔值
            修改操作符:
                $set:修改一个域的值或者增加一个域,可以同时修改多个域
                $unset:删除一个域 db.class0.updateOne({name:'小明'},{$unset:{sex:''}}) db.sales.updateMany({$or:[{year:2016},{item:'B'}]},{$unset:{quantity:''}})
                $rename:给域重命名 db.class0.updateMany({name:{$exists:false}},{$rename:{name:'1'}}
                $setOnInsert:如果使用update*执行了插入文档操作,则作为插入内容(upsert为true,并执行了插入操作,而不是修改操纵)
                $inc:加法修改器 --> db.class2.updateMany({},{$inc:{age:1}})
                $mul:乘法修改器 --> db.class2.updateMany({},{$mul:{age:2}})
                $max: 修改某个域的值,如果小于指定值则修改,大于则不变 --> db.class2.updateMany({sex:'w'},{$max:{age:30}})
                $min:用法类似max

                Array
                $push 向数组中添加一项 --> db.class2.updateOne({name:'夏天'},{$push:{score:10}})
                $pushAll 向数组中添加多项 --> db.class2.updateOne({name:'谷雨'},{$pushAll:{score:[15,45]}})
                $pull 从数组中删除某个值(如果这个值有多个一并删除)   |
                $pullAll 从数组中删除多个值                      |用法同上
                $pop:弹出数组中一项 -->db.class2.updateOne({name:'春天'},{$pop:{score:1}}) 1弹出最后一个,-1弹出第一个
                $addTOSet:向数组中添加一项但不能重复 --> db.class2.updateOne({name:'春天'},{$addToSet:{score:80}})
                $each:对多个值逐一操作 --> db.class2.updateOne({name:'秋天'},{$push:{score:{$each:[99,0]}}})
                $position:指定数组插入的位置配合$each --> db.class2.updateOne({name:'谷雨'},{$push:{score:{$each:[10],$position:1}}})
                $sort:配合pull和each使用--> db.class2.updateOne({name:'秋天'},{$push:{score:{$each:[],$sort:1}}}) 1升序-1降序


        db.class.update(filter,update,upsert,multi)
        db.class0.findOneAndUpdate( filter, update, <optional params> )
            - update first matching document,
              optional parameters are: projection, sort, maxTimeMS, upsert, returnNewDocument
        db.class0.findOneAndReplace( filter, replacement, <optional params> ) - replace first matching document, optional parameters are: projection, sort, maxTimeMS, upsert, returnNewDocument
            替换文档,replacement的形式不需要update操作符,而是相当于插入语句

exesecise:
    1.db.class0.updateOne({name:'小红'},{$set:{hobby:['dance','draw'],age:8}})
    2.db.class0.updateOne({name:'小明'},{$push:{hobby:'sing'}})
    3.db.class0.updateOne({name:'小王'},{$pushAll:{hobby:['sing','basketball']}})
    4.db.class0.updateOne({name:'小李'},{$addToSet:{hobby:{$each:['running','sing']}})
    5.db.class0.updateOne({name:'小明',{$unset:{sex:''}}})
    6.db.class0.updateOne({name:'小李',{$pop:{hobby:-1}}})
    7.
    8.

    5.删除操作
        1.db.class0.deleteOne(query) --> db.class0.deleteOne({gender:{$exists:false}})
        2.db.class0.deleteMany(query) --> 同上
        3.db.class1.findOneAndDelete(query) 返回查找到的文档

db.class.deleteMany({$or:[{age:{$lt:8}},{age:{$gt:12}}]})
db.class.deleteMany({hobby:{$nin:['draw','dance']}})


exercise:
    1.db.class.updateOne({name:'小红'},{$push:{hobby:{$each:['sing'],$position:1}}},{upsert:true})
    2.db.class.updateOne({name:'小王'},{$set:{nation:{'民族':'回族','习俗':'注意饮食禁忌'}}},{upsert:true})
    3.db.class.updateOne({name:'小王'},{$rename:{nation:'info'}})
    3.db.class.updateOne({name:'小王'},{$set:{'info.宗教':'伊斯兰'}})

索引操作:
    索引是建立文档所在位置的查找清单,使用索引可以方便快速查找,提高查找效率.
    db.class.createIndex()创建索引,参数位索引域和索引选项
        -->db.class0.createIndex({name:1}) 参数1:在name域上创建正向索引,1正向,-1逆向
        -->db.class0.createIndex({age:-1},{name:'姓名索引'}) 参数2:索引名称
        -->db.class0.ensureIndex() == db.class.createIndex()
        -->db.class0.createIndexes([{},{},{}...]) 可以创建多个索引
    db.class.getIndexes()查看集合中索引
    db.class.dropIndex()删除索引,参数为索引名称或者索引键值对
        -->db.class0.dropIndex('name_-1')
        -->db.class0.dropIndex({age:-1})
    db.class.dropIndexes()删除所有索引(_id索引不会被删除)
    复合索引:根据多个域创建一个索引
        -->db.class0.createIndex({name:1,age:-1},{name:'composite_index'})
    object/数组索引:如果对子文档域或者数组域创建索引,则针对object或者数组中的某个元素的查询也是索引查询
    唯一索引:要求创建索引的域不能有重复的值
        -->db.class0.createIndex({name:1},{unique:true})
    稀疏索引:如果有些文档中创建索引的域不存在,则不在此文档创建索引
        -->db.class0.createIndex({age:1},{sparse:true,name:'sparse'})

聚合操作:对文档进行数据整理统计得到统计结果
    db.class.aggregate()执行聚合操作,参数为聚合条件配合聚合操作符使用
    聚合操作符
    $group 分组聚合 需要配合一些统计操作符
    -->db.class0.aggregate({$group:{_id:'$gender',num:{$sum:1}}})
    -->db.class0.aggregate({$group:{_id:'$gender',num:{$sum:'$age'}}})
    -->db.class0.aggregate({$group:{_id:'$gender',avg:{$avg:'$age'}}})
    -->db.class0.aggregate({$group:{_id:'$gender',max:{$max:'$age'}}})
    -->db.class0.aggregate({$group:{_id:'$gender',min:{$min:'$age'}}})
    -->db.class0.aggregate({$group:{_id:'$gender',min:{$min:'$age'},max:{$max:'$age'},avg:{$avg:'$age'}}})
    -->db.class0.aggregate({$group:{_id:'$gender',first:{$first:'$age'}}})
    -->db.class0.aggregate({$group:{_id:'$gender',last:{$last:'$age'}}})
    $match 匹配和筛选数据 同query参数只是外扩了一个match
    -->db.class0.aggregate({$match:{age:{$gt:18}}})
    $limit 获取集合中前几条文档
    -->db.class0.aggregate({$limit:3})
    $skip 跳过前几个个文档 同find
    $sort 排序 同find
    $project 重新显示文档中的域,db.class0.aggregate({$project:{_id:0,name:1}}) 1代表显示0代表不显示 显示的域可以是重新计算得到的域
聚合管道:
    db.class.aggregate([{},{},....])
    将前一个聚合产生的结果交给后一个聚合继续操作,直到最后的结果
    -->db.class0.aggregate([{$group:{_id:'$name',num:{$sum:1}}},{$match:{num:{$gt:1}}}])

exercise:
    db.class.find({sex:'m'},{_id:0}).sort({age:1})
    db.class.aggregate([{$match:{sex:'w',hobby:'draw'}},{$project:{name:1,age:1,hobby:1,_id:0}},{$sort:{age:1}},{$limit:3}])


固定集合:
    db.createCollection(collection,{capped:true,size:10000,max:20})

文件存储思路:
    1.将文件路径存储在数据库中
    2.存储文件本身

GridFS文件存储方案: 一般用于大于16m
    1.mongoDB数据库中创建两个集合共同存储文件
    2.fs.files集合中为每个文件建立一个信息文档,存储文件的基本信息
    3.fs.chunks集合中每个文档建立和fs.files的关联,并将文件分块存储

    存储方法:
    mongofiles -d 数据库名称 put 文件地址/文件名称  -->  mongofiles -d grid put Postman.tar.gz
    读取方法:
    mongofiles -d 数据库名称 get 文件地址/文件名称

    ps:mongo shell 支持基本的js代码,可以通过js处理mongo的一些数据逻辑


'''
