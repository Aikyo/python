import os
import re


"""

27、比较： a = [1,2,3] 和 b = [(1),(2),(3) ] 以及 b = [(1,),(2,),(3,) ] 的区别？
a = [1,2,3]正常的列表
b = [(1),(2),(3)] 虽然列表的每个元素加上了括号，但是当括号内只有一个元素并且没有逗号时，其数据类型是元素本身的数据类型
b = [(1,),(2,),(3,)]列表中的元素类型都是元组类型
--------------------- 
作者：春雨里de太阳 
来源：CSDN 
原文：https://blog.csdn.net/qq_16633405/article/details/88354065 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
str1 = "today is your day,tommorrow is your day"
a = int('1')
print(a)

a = ['1','2','3']

b = []
for x in a:
    b.append(int(x))

print(b)

