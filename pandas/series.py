import pandas as pd

#1.create
lst1 = [1,2,3,4,5,6,7]
s1 = pd.Series(lst1,index=list('abcdefg'))
print(s1)






#2.access
"""
slice 后还是series
index后是值
series[:] 
series.loc

"""

print(s1['a'])
print(s1.iloc[0])

#slice output still a series
print(s1[:2])
#print(s1.loc[0:1])
s2 = pd.Series(list('qwertyuiop'))
print(s2)
s3 = s2.loc[0:5]
print('-------------')
print(s3)
print(s2[0:5])
print('index取值')
print(s2.iloc[0])
print(s2[0])
print("loc 永远是series")
print(s2.loc[0])
print('ddd')
print(s2.iloc[:3])
print(s2.iloc[:1])


# 3.binary operation
"""
1.fill series till same dimention
series1.add(series2,fill_value=0)
series1.sub(series2,fill_value=0)

"""
s5 = pd.Series([int(x) for x in list('123456789')])
print(s5.mean())
print(s5.sum())
# 4.conversion operation
"""


"""





