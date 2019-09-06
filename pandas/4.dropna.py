import pandas as pd

"""
drop null value avoid error


"""


#part 1 series dropna

se1=pd.Series([4,None,8,None,5])
print(se1)
print(se1.dropna())
print('-------------------------')
print(se1[se1.notnull()])


#part 2 dataframe dropna
"""
parameter 
how='any'
axis=0
inplace : if ture do operation inplace else create new one

df.dropna() 
df.dropna(how='all') 所有都是null的行
df.dropna(how='any') 只有要null的行
df.dropna(thresh=2) 大于两个null的行

df.dropna(axis=1) 操作列

"""


data = pd.DataFrame({'name':'herman,kiko,alia'.split(','),'age':list('123')})

df1=pd.DataFrame([[1,2,3],[None,None,2],[None,None,None],[8,8,None]])

df1.dropna(how='any',inplace=True)
print(df1)



















