"""
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
同时用到index 和 value
"""
list1 = [1,2.34,5.6,23]
a = enumerate(list1)
print(type(a))