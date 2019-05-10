"""
string 常用方法
replace strip split upper lower join find index

"""
#replace
str1 = "i am am am kiko"
str2 = str1.replace('am','zhongkang',2)
print(str2)

s1 = str1.split("k")
print("s1 split : ",s1)

s2 = str1.upper()
print(s2)
r1 = str1.find("am")
print("find index :",r1)
r2 = str1.index("ko")
print("index result :",r2)
s4 = " hello i am {0}".format("zhongkang")
print(s4)

print("--dict head------------------------------------------------")
"""
dic 常用方法
"""
d1 = {}
d1['feifei'] = 1
d1['zilong'] = 2
d1['beibei'] = 3
d1['guanguan'] = 4

ld1 = [x for x in d1.keys()]
print(ld1)
d2 = dict(zip(d1.values(),d1.keys()))
print("zip d1 :",d2)
ld2 = list(zip(d1.values(),d1.keys()))
print("ld2 :",ld2)

print(d1.keys())
print(d1.values())



print(len(d1))

d1['仲谋'] = len(d1)
print(' after zhongmou ',d1)


"""
set attribute and function
"""
l1 = ['xiaofeifei','zilong','guanguan','beibeige','zhongzhong','zilong']
s1 = set(l1)
print(s1)
l2 = list(s1)
print("l2 :",l2)
s3 = {}
print(type(s3))

print("_ head ------list____________________________________________________________________-")
"___________list____________________________________________________________________-"
"""
list attribute and function
"""
import collections
l1 = ['xiaofeifei','zilong','guanguan','beibeige','zhongzhong','zilong']
l2 = ['奉先','奉孝']

#1.count and list a element in a list
a = collections.Counter(l1).most_common(2)
print(a)

#2.extend = add list
l1.extend(l2)
print(l1)

#pop last one of the list
print(l2.pop())
print(l2)


#insert
l2.insert(4,'蒙德')
print(l2)


#count element in the list
print(l1)
print(l1.count("zilong"))

#sort list
l3 = [2,34,5,3,1,55,321]
l4 = [('1',1),('33',42),('rr',9)]
l3.sort()
print(l3)
print(max(l3))
print("_ tail ------list____________________________________________________________________-")
""