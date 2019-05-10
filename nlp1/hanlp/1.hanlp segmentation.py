#encoding=utf8
from jpype import *
startJVM(getDefaultJVMPath(),"-Djava.class.path=D:\A_NLP\hanlp\Hanlp\hanlp-1.7.2.jar;D:\A_NLP\hanlp\Hanlp",
         "-Xms1g",
         "-Xmx1g")

cuba = r'美国驻古巴使馆代办玛拉·特卡15日在社交媒体宣布，从本月18日起，古巴' \
       r'民众在第三国申请赴美签证时将不再获得有效期为5年的多次往返签证，而改为' \
       r'单次入境签证、每次获准在美国停留3个月。'

c1 = "中国科学院计算机研究所研究员钟康正在和奶茶！"
hanlp = JClass('com.hankcs.hanlp.HanLP')
list1 = hanlp.segment(c1)
print("standard : ",list1)

StandardTokenizer = JClass('com.hankcs.hanlp.tokenizer.StandardTokenizer')
tokenizer1 = StandardTokenizer.segment(c1)
print('tokenizer : ',tokenizer1)

#索引分词
#index tokenizer
indexTokenizer = JClass('com.hankcs.hanlp.tokenizer.IndexTokenizer')
termlist = indexTokenizer.segment('雨打蕉叶又潇潇了几夜')
print([str(x) for x in termlist])
for term in termlist:

    print(str(term) + " : " + str(term.offset) + ":" + str(term.offset + len(term.word)))


#自定义分词
CustomeDictionary = JClass("com.hankcs.hanlp.dictionary.CustomDictionary")
CustomeDictionary.add("单身狗")
ss1 = hanlp.segment("单身狗的快递像是冬天最寒冷的那一天下起了雨！")
print(ss1)


summary1 = hanlp.extractSummary(cuba,9)
print(summary1)

keywords = hanlp.extractKeyword(cuba,8)
print(keywords)

phrases = hanlp.extractPhrase(cuba,6)
print(phrases)