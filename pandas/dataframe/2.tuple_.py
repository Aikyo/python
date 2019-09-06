import pandas as pd
import numpy as np


t1 = (12,'content')

s = pd.Series(t1).T
print(s)
df = pd.DataFrame(s,columns=['a'])
print(df)
print('------------------------')
print(df.T)










