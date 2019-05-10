import jieba
import jieba.analyse
import jieba.posseg

def cut_words(sentence):
    return " ".join(jieba.cut(sentence))
f = open('guoqinlun.txt',mode='r')
lun = f.read()
lun_cut = cut_words(lun)
#print(lun)
print(lun_cut)

