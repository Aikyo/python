import pickle


li = [11,22,33]
pickle.dump(li,open('p1','wb'))

#load
ret = pickle.load(open('p1','rb'))
print(ret)