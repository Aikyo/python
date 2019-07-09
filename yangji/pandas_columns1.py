import pandas as pd
import numpy as np

arr = np.random.normal(1,0.5,9).reshape(3,3)
print(arr)

d1 = pd.DataFrame(arr,columns=['a','b','c'])
print(d1)

d1['e'] = [3,3,3]
print(d1)
print(d1['e'])
print(len(d1['e']))

d1[0,'a'] = [1,2,3]








