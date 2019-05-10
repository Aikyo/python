#encoding=utf8
import jieba
#jieba.load_userdict("mydict.txt")
jieba.add_word("折枝先生")
a = jieba.cut("你好我是折枝先生，你在东京吃草好玩吗")
a1 = " ".join(a)
print(a1)




