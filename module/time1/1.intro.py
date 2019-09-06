from datetime import datetime
import time


# get timestamp timestamp单位是秒
print(time.time())

# standard stimestamp
print(time.strftime('%Y-%m-%d %H-%M-%S'))
print(time.strftime('%H:%M:%S'))


# timestamp to time
print(time.localtime(time.time()))

# timestamp to time
print(datetime.fromtimestamp(1564563462.9089134))
print(datetime.fromtimestamp(1564563362.9089134))

#相差一百秒
a = 1564563462.9089134 - 1564563362.9089134
print(a)
print(datetime.fromtimestamp(0))
print(datetime.fromtimestamp(a))



