'''

    小文件存储?
    二进制存储数据类型转换
    content = bson.binary.Binary(bytes):将python字节穿转换为bson格式

'''

from pymongo import MongoClient
import bson

conn = MongoClient('127.0.0.1', 27017)
db = conn.images
myset = db.jinguanzhang

# ==============================
'''
# 存储图片
with open('fig.jpg','rb') as f:
    data = f.read()

# 将data转化为bson格式
data_bson = bson.binary.Binary(data)

# 将图片变为一个文档-->插入集合中
dic = {'filename':'jinguanzhang','data':data_bson}
myset.insert_one(dic)

'''
# ================================
# 提取文件 --> 查找出写入本地
file = myset.find_one({'filename':'jinguanzhang'})
with open('fig1.jpg','wb') as f:
    f.write(file['data'])


conn.close()