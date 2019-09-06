lst = [1,2,3]
try:
    a = lst[100]
except Exception as e:
    print(e)
    a = 'meiyou'

print(a)


import re

s1 = '3443gg5656hh777'
lst = re.findall('\d+',s1)
print(lst)
matcher = re.match('\d+',s1)
print(matcher.group())




