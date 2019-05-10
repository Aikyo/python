
"""

is:判断内存地址是否相等
==：判断数值是否相等

"""
a = []
b = [1]
c = a
print(id(a))
print("c ",id(c))
print(a is c)

print(a == c)
print(a == b)
print(id(b))