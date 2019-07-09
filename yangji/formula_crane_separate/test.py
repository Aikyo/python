import pandas as pd

lst = [1,2,3,4,5,6,7,8,9,10]

b = pd.cut(lst,[0,6,10],labels=['a','b'])

print(b.tolist())


data = {
    '天车':['A','B','C','D','E', 'H','I','J','K'],
    '工作区间':['115','1520','207','3743','4355','5561','6177','7784','8493']
        }

data1 = pd.DataFrame(data)
print(data1['天车'][2])

print(type(data1['天车']))


print(data1)

print(data1.loc[data1['天车'] == 'H'])

d3 = data1.loc[data1['天车'] == 'H']
print('---------------------------------------------')
print(d3[0:1]['工作区间'] * 2 )

print(type(d3[0:1]['工作区间'] * 2))
o = d3[0:1]['工作区间']*2
print(o.iloc[0])






