import pandas as pd
d1 = pd.DataFrame({'a':10,'b':11},index=['age'],columns=['kiko','herman','a'])

print(d1)
d2 = pd.isnull(d1)
print(d2)
print(~d2)
d3 = d1[~d2.loc[0,:]]



print(d3)







