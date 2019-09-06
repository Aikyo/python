import json


name = {'name':'herman'}
str1 = json.dumps(name)
print(str1)
d = json.loads(str1)
print(type(d))
print(d)


