from urllib import request

url = "http://www.baidu.com"
response = request.urlopen(url)
print(type(response))
page = response.read()
print(page)


import numpy as np
a = np.ndarray(shape=(4,1),dtype=np.int32)
print(a)

b = np.array([1,23,4])
print(type(b))

c = np.array(shape=(1,3))
print(c)




