#encoding=utf8
count = 0
fo = open(r'D:/herman2.txt','r')
line = fo.read()
for li in fo:
    count +=1
print(line)
print(count)

"""
write
mode a append 
mode w override
"""
fr = open(r'D:/herman.txt','a')
fr.write(line)
fo.close()
fr.close()