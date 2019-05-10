import jieba.posseg as pseg

f = open("端午的咸鸭蛋",mode='r',encoding='utf8')

ss = f.read()
str1 = pseg.cut(ss)
str2 = ""
for i in str1:
    str2 += str(i) + " "


f1 = open("yadanpo8seg59.txt",'x')

f1.write(str2)
