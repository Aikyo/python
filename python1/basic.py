def getLines():
    with open('C:/herman1.txt','w') as f:
        return f

fo = open('D:/herman2.txt','a')
print(fo.name)
string = "i won't be happy anymore!"
fo.write(string)
fo.close()
"""
model a:append w:覆盖
"""


fo = open('D:/herman2.txt','r')
herman = fo.read()
print(herman)
fo.close()


"""
1. z,staticmethod don't need self , instance 
2.
"""
class A():
    def show(self,x):
        print(x)
    def printf(cls,y):
        print(y)
    def writeline(z):
        print(z)

a = A()

a.show("x---instance method")
A.show(a,"instance method")

a.printf("y")
A.printf(A,"classmethod")
A.writeline("z")

"""
class variable
instance variable 
"""
print("3")


class INS_Cl():

    num = 0
    name = 'kiko'

    def __init__(self,name):
        self.name = name
        INS_Cl.num += 1

    @property
    def show(self):
        print("property method -------hello kiko") #property method need instance object

    @staticmethod
    def print():
        print("static method")


i1 = INS_Cl("herman")
print("property")
i1.show
i3 = INS_Cl("jim")
INS_Cl.name = "jeff"
print(i1.name)
print(INS_Cl.name)
print(i1.num)
i1.num = 45
print(i1.num)
INS_Cl.print()


"""
自省,取址
"""
#print(type(3))
a = [1,2,'33']
b = {2,'55'}
c = (2,3,)
print(type(a))
print(type(b))
print(type(c))


"""
iterable 
generator
yeild
"""
kiki = "kiki's deliver services"
for i in kiki:
    print(i)

print("slice-------")
print(kiki[1])


print("iterator : any sequence is an iterator")
iter1 = [x*x for x in range(5)]
for i in iter1:
    print(i)
for i in iter1:
    print(i + 2)



print("generator : "  \
       "Generators do not store all the values in memory," \
       "can only iterate over once  "
      "they generate the values on the fly:")

r1 = (x**x for x in range(4))
for i in r1:
    print(i)
for i in r1:
    print(i + 1)

print("yield ")

def Generator():
    list = range(4)
    for i in list:
        yield  i*i

generator  = Generator()
print(generator)
for i in generator:
    print(i)
print(generator)
print("second time test generator")
for i in generator:
    print(i)

print("---------datetime--------")
"""
datetime
"""
import time
import datetime
print(time.time())
print(time.localtime())
print(time.asctime())
print(time.clock())
t1 = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(t1)

import calendar
cal = calendar.month(2019,3)
print(cal)
# year = input("year ")
# month = input("month ")
# day = input("day " )
# date1 = datetime.date(year=int(year),month =int(month),day =int(day))
# print(date1)


"""
random 
"""
import random
list1 = [1,2,3,4,5]
random.shuffle(list1)
print(list1)


"""
sort : list.sort()
sorted : return a new sequence
"""
arr1 = [2,4,1,5,3]
arr2 = sorted(arr1)
print(arr2)
arr1.sort()
print(arr1)

print("dic-----------------------")
dic1 = {"b":78,"a":1,"c":6}
print(dic1)
dic2 = sorted(dic1)
print(dic2)
dic3 = sorted(dic1,reverse=True)
print(dic3)

dic4 = sorted(dic1.items(),key=lambda x:x[1])
print(dic4)
dic5 = sorted(dic1.items(),key=lambda x:x[0])
print(dic5)

str4 = "iamkiko"
print(str4[1:4])
print(str4[::-1]) # head:tail:step

# dic6 = {key:value for (key,value) in ["a","c","v"]}
# print(dic6)

dic = {}
str1 = "k:1|k1:2|k2:3|k3:4"
for items in str1.split("|"):
    key,value = items.split(":")
    dic[key] = value
print(dic)
dic['k'] = 2
print(dic)

alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]

alist1 = sorted(alist,key= lambda x:x['age'])
print(alist1)

print([x*11 for x in range(6)])

set1 = {1,3}
print(type(set1))



