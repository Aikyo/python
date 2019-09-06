import pandas as pd

import numpy as np

data = np.random.normal(1,0.2,9).reshape([3,-1])
df = pd.DataFrame(data,columns=list('abc'))
print(df.dtypes)
print(df)
df['a'] = df['a'].round(1)
# df2 = df.round({'a':1,'b':2,'c':3})

print(df)
