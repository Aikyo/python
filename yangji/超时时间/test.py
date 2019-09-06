d1 = {1:[7,7,7],2:[8,8,8],3:[6,6,6]}

import pandas as pd

data = pd.DataFrame(d1,index=['甘薯','kiko','jj']).T.rename({0:'甘薯'})
print(data)
sum1 = 0
# for x in data['kiko']:
#     print(x)
#     print('--------')
def func(df):
    global sum1
    sum1 += df['jj']
    return sum1
d1 = data.apply(func,axis=1)
print(d1)
print(sum1)
data['jj'] = data['jj'].map(lambda x:x+1)
print(data)