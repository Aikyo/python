import numpy as np
import pandas as pd

arr = np.random.normal(1,0.0001,3)
print(arr)
s1 = pd.Series(arr,name='kiko',index=list('abc'),dtype=np.float32)

print(s1)
















