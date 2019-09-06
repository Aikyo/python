import pandas as pd


data = {'name':'herman,jeff,lebrown,kiko'.split(','),'score':[int(x) for x in '9887'],'age':[int(x) for x in '3657']}
data = pd.DataFrame(data)

d1 = data.sort_values(by=['score','age'],ascending=False)
print(d1)

print(data.index)

data.insert(0,'id',0)
print(data)

filter = data['score'] > 3
filter2 = data['age'] > 3
d2 = data.where(filter&filter2)
d2.dropna(how='all',inplace=True)

print(d2)
print('---------------------------------------------------------------------')
print(data)
d3 = data.query("score >= 7 and age >=6")
print(d3)



print('----------------')
#duplicated
data.loc[4] = [1,'momo',12,10]
data.loc[5] = [1,'momo',12,10]
data.sort_values(by=['score','age'],inplace=True,ascending=False)
print(data)
a = data.duplicated()
print(data[~a])


print('========================')
print(data)
s1 = data['name'].rank()
print(s1)
data['Rank'] = s1
print(data)
#print(data.sort_values(by=['name']))
print(data.rank(axis=0))



# def mean_of_score_age():
#









