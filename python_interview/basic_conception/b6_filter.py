
"""
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。

该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，
然后返回 True 或 False，最后将返回 True 的元素放到新列表中。


"""

def is_odd(s):
    return s%2 == 0

a = list(filter(is_odd,(1,23,4,5,6,7,8)))
print(a)

b = filter(lambda x:x**2,(2,3,4))
print(type(b))
c = list(b)
print(c)

