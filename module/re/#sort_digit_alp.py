import re
import random



d1 = [{'id':'12'},{'id':'33-34'},{'id':'33-34'},{'id':'d3-34'},{'id':'electric'},{'id':'2'},{'id':'122'},{'id':'f4545'}]

d = sorted(d1,key=lambda x: int(re.match('\d+',x['id']).group()) if re.match('\d+',x['id']) else 10000)

print(d)

#random.randint(-1000,1000) + 10000











