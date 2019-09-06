import json

f = open('pole2.txt',mode='r',encoding='utf-8')
a = json.loads(f.read())
print(a)





