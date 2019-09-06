import pandas as pd
import numpy as np


data = np.random.normal(1,0.1,9).reshape([3,-1])
dict1 = {i:x for i,x in enumerate(data)}
df = pd.DataFrame(dict1,index=['first','second','third']).T
print(df)

# 1.access to row
print(df.loc[0])
print(df.iloc[0])
print(type(df.loc[0]))


# 2.access to columns
print(df['first'])
print(type(df['first']))


# 2.access to specified row and column
print(df.iloc[1,1])
print(type(df.iloc[1,1]))

print('--------------')
print(df.loc[1,['second']])
print(type(df.loc[1,['second']]))
df1 = df.loc[1,['second']]

print(df1[0])

if df1[0] > 1:
    print('great than 1')
else:
    print('less than 1 ')

print(type(df1[0]))

