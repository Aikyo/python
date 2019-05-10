import jieba
import re

f = open("jidushan.txt")
file = open('jd.txt','w',encoding='utf-8')
b = f.readline()

for line in f:
      line1 = re.sub(r'[\s，。？?！“”‘’…：；:（）《》、—.．*~～＿－-]','',line)
      file.write(line1)
file.close()
print(b)

