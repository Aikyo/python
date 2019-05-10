from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'D:\A_NLP\stanford_nlp\stanford_corenlp',lang = 'zh')
fir = open('D:\herman2.txt','r')
fiw = open('D:/herman.txt','w')
cixing = open('D:/cixing11.txt','a')

for line in fir:
    line = line.strip()
    if len(line) < 1:
        continue
    fiw.write(" ".join([each[0]+"/" +each[1] for each in nlp.ner(line) if len(each)==2 ]) + "\n")
    # cixing.write(" ".join([each[0] + "/" + each[1] for each in nlp.pos_tag(line) if len(each) == 2]) + "\n")

fir.close()
fiw.close()
cixing.close()