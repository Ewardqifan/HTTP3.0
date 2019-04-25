'''
    import re

    re.findall('正则表达','xxx,xxx,xxxx')


总结:
    匹配字符: '.' '[]' 'x|x' '\D' '\d' '\W' '\w' '\s' '\S' '\D' '\d'
    匹配重复: '*' '+' '?' '{x}' '{x,x}' '\A' '\Z' ps:非贪婪模式在后加?
    匹配位置: '^' '$' '\b' '\B'

regex = re.compile(pattern,flags)
生成正则表达式对象
pattern:正则表达式
flags:功能扩展标志位
返回:正则表达式对象

list = re.findall(pa,str,fl)      regex.findall(str,pos,endpos)
pa:正则                               srt:目标字符串
str:目标字符串                         pos:截取目标字符串开始位置
返回:匹配到的列表                       endpos:截取目标字符串的结束位置

list = re.split(pa,str,flag=0)
返回分割后的字符串

s = re.sub(pa,rel,str,count,flag=0)
使用指定字符串替换匹配到的内容
rel 指定字符串
count 替换多少处 默认全部替换
返回替换后的字符串

iter = re.finditer(pa,str)
返回match对象
通过iter.group()方法转化为字符串

re.fullmatch(pa,str) # 完全匹配 相当于在前加^在后加$
返回一个match对象

re.match(pa,str,flag=0)
匹配目标字符串起始内容  # 相当于在前加^
返回match对象

re.search(pa,str)
匹配第一处符合条件的match对象


match 对象的属性:pos,endpos,re,string,lastgroup,lastindex
        funs:group,groups,pos,endpos
'''
# match words with UP alpha in the file
# find out numbers of int decimal >0 <0 x/x x%
# find date and replace (2019-1-3) -> 2019.1.3

import re

'''
# work 1
# str = 'I want the hunger for love and beauty to be in the\r\n'
# str += 'Depths of my spirit , for I have been seen those who are\r\n'
# str += 'Satisfied the most wretched of people\r\n'
# str += 'I have heard the sigh of those in yearning and Longing , and it is sweeter than the sweetest melody'

PATH = './test.txt'

# with open(PATH,'wb') as fw:
#     fw.write(str.encode())

with open(PATH,'rb') as fr:
    data = fr.read()


# Up_words = re.finditer('[A-Z][a-z]*',data.decode())
# for i in Up_words:
#     print(i.group())

print(re.findall('\S+',data.decode()))
'''
# work 2
str01 = '-15.55548,100,98.2%,78/52,zhe,-78/55'
# >0
# print(re.findall(r'[^-]|\,[^,]', str01))
# <0

# int
print(re.findall(r'\b\d+\b',str01))
# decimal

# x/x

# x%

# work 3

# str02 = '(2019-1-5),(2018-6-7),awa,12589'
# print(re.sub(r'\(.{8,10}\)','2019.1.3',str02))