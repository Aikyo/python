import time

ctime = time.time()
print(ctime)


localtime = time.localtime(ctime)

print(localtime)
print(time.localtime())


import datetime
c_time = datetime.datetime.now()

delta_time = datetime.timedelta(days=7)

c_time = c_time - delta_time
print(c_time)


##set
print("-------------set-----------------")

d1 = {'a':1,'b':2,'b':2}
d2 = {'c':3,'b':2}

s1 = set(d1.items())
s2 = set(d2.items())
print(s1)
print(s2)
print(type(s1))
s3 = s1 - s2
print(s3)
