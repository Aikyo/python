from stanfordcorenlp import StanfordCoreNLP


nlp = StanfordCoreNLP(r'D:\A_NLP\stanford_nlp\stanford_corenlp', lang='zh')
f1 = open('yuda.txt', 'r',encoding='utf8')
# fiw = open('jiaoye.txt','a')
cixing = open('xiaoxiao13.txt', 'x')
for line in f1:
    line = line.strip()
    if len(line) < 1:
        continue
    cixing.write(" ".join([each[0]+"/" +each[1] for each in nlp.ner(line) if len(each)==2 ]) + "\n")
    cixing.write(" ".join([each[0] + "/" + each[1] for each in nlp.pos_tag(line) if len(each) == 2]) + "\n")

#fir.close()
# fiw.close()
cixing.close()

