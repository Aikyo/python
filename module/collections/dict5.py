d1 = {'a':1,'b':2,'c':3}
for x,y in d1.items():
    print(x)

# lst1 = [x for x in d1.items() if x.startswith('a')]
# print(lst1)
str1 = '1234560'
if str1.startswith('123'):
    print('123')
print(str1.isnumeric())

print(str.isnumeric(str1))
# print(str.isnumeric(None))
print(isinstance(None,str))





