import pandas as pd
import numpy as np


arr = np.random.normal(1,0.01,9).reshape([3,-1])
df = pd.DataFrame(arr,columns=list('abc'))

print(df.index)
df.name = 'ddss'
print(type(df.index))
#print(df.name)
print(df)



s1 = pd.Series(list('abcdefg'))
s1.name = 'dd'
print(s1)
print(s1.index)









