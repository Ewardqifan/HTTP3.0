import os
import sys

# sys是在os上的一个封装模块，为了更方便python用户使用
# 结束进程，参数含义人工设计一般，0代表正常结束，
# 类似sys.exit([]) 可选参数　默认为0　
# 整数表示退出状态;字符串表示退出时打印内容,以异常形式打印

print(os.getcwd())
print(os.path.split(os.getcwd())[-2])

# sys.exit(['aaaa'])
# os._exit(0)
# print('process over')
