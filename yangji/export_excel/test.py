import pandas as pd

name = {"names":"herman,kiko,zhangfei,feifei","age":list('3654')}

df =pd.DataFrame(name)
#df = df.unstack()
print(df.columns.levels[0])



