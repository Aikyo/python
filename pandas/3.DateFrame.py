import pandas as pd

data = pd.DataFrame({'name':'herman,kiko,muziki'.split(','),'age':[int(x) for x in '123']})
print(data)

# part 1 access
"""
 The df.iloc indexer is very similar to df.loc but only uses integer locations to make its selections.


"""
#colums index -> series
print(data['age'])
print(type(data['age']))

#columns index by a list [] -> dataframe

print(type(data[['name','age']]))

data = pd.DataFrame({'name':'herman,kiko,muziki'.split(','),'age':[int(x) for x in '123']})


print(data)
print(data.loc[2])
print(data.iloc[2])







