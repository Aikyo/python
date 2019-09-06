import json
import pandas as pd


data = json.loads('[{"index":1,"slot":"93","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":2,"slot":"55","standard_time":1,"max_time":1,"load_module":"","load_value":"1"}]')
df = pd.DataFrame(data)

print(df)
print(type(df.iloc[0,2]))
print(df.iloc[0,3])
values = df['load_value']
print('---')
print(values)
df['load_value'] = values.replace(to_replace='', value='0')
print('-=----------------')
print(df)







