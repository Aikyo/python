import numpy as np
import pandas as pd

arr1 = np.arange(1,10)
print(arr1)
s1 = pd.Series(arr1)
print(s1)


arr2 = arr1.reshape((3,3))

print(arr2)

d1 = {1:'kiko',2:'herman'}
arr3 = pd.Series(d1)
print(arr3)








