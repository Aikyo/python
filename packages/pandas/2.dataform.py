import pandas as pd
import numpy as np

arr1 = np.arange(0,9).reshape((3,-1))
print(arr1)
data1 = pd.DataFrame(arr1)

print(data1)


d1 = {'a':[1,23,4,5],'b':[2,3,4,5]}

data2 = pd.DataFrame(d1)

print(data2)


