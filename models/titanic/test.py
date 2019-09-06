import pandas as pd
d = {"name":['herman','kiko'],"age":[1,2]}
df = pd.DataFrame(d)
print(df)


s1 = df['name']
print(s1)
s2 = s1[s1 == 'herman']
print(s2)

df.query()











