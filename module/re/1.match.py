import re

s1 = '789-784'
r1 = re.match('^(\d+)[^\d]*',s1)
# print(r1.group())
r11 = re.match('\d+',s1)
print(r11.start())
print(r11.end())
print(r11.group())
print(r11.groupdict())


r2 = re.findall('\d+',s1)
print(r2)

r3 = re.match('[\d]*','786-415-96')
print(r3.group(),'  r3')

r4 =re.match('^(\d+)[^\d]*', '78-45-56')
print(r4.group())



