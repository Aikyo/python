from jieba import analyse

text = r"其次因为香港是一个寸金寸土的地方，先不说它的房子价格有多么的高，" \
       r"我们如果要去香港游玩的话住宿方面就需要花费不少的钱，普通的民宿住一" \
       r"晚上都需要花费400港币左右，也就是人民币300元，更不要说酒店了住一晚上" \
       r"大概需要花费800以上港币也就是人民币600元以上。住的方面如果我们玩一段时" \
       r"间就需要花费许多，一万元人民币顶多让你住十多天。" \
       r"漂亮美丽无敌"
keywords = analyse.textrank(text,withWeight=True,allowPOS=('n','ns','a'),withFlag=True,topK=5)
for word in keywords:
    print(word)
    #print(type(word[0]))

tags1 = analyse.extract_tags(text,withFlag=True,withWeight=True,topK=5)
for word in tags1:
       print(word)





