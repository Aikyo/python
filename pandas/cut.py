import pandas as pd
import numpy as np
ages = np.array([1,5,10,40,36,12,58,62,77,89,100,18,20,25,30,32])
a = pd.cut(ages, [0,10,25,100])
print(type(a))
print(a)














