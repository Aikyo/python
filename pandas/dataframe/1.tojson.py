import pandas as pd
import numpy as np

data = np.random.normal(1,0.1,9).reshape([3,-1])
df = pd.DataFrame(data,columns=list('abc'))
print(df)
print('------------------')
print(df.to_json(orient='split'))
print('++++++++++++++++')
df.reset_index().to_json(orient='records')
print(df.to_json(orient='records'))
print('-------直接tojson---------')
print(df.to_json())







