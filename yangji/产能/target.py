import pandas as pd
from Table.yangji import TableOperation


table = TableOperation()
#连接数据库
conn = table.get_py_connect()
#获取数据
query_sql = 'select `name`, target_num from target_num'
#生成字典
d1 = table.query_tuple_table(conn, query_sql)
print(d1)
print('----------------')
target_dict = dict(table.query_tuple_table(conn, query_sql))
print(target_dict)
print(pd.DataFrame(target_dict, index=['quota']))
target_ = pd.DataFrame(target_dict, index=['quota']).T
print(target_)

target_['pfname'] = target_.index
data = pd.read_sql('select no, name, quantity from material where name not like "!EP%"', conn)

print(type(data.groupby('name')))

freq_df = data.groupby("name")[['no']].count().reset_index().rename({'no': 'done', 'name': 'pfname'}, axis=1)
print(freq_df[:5])
# test_df = data.groupby("name")['no'].count().rename({'no': 'done', 'name': 'pfname'}).reset_index()
# print(test_df[:5])


freq_df = pd.merge(left=target_, right=freq_df, on='pfname', how='left').fillna(0).reset_index(drop=True)

print('-----------')
print(freq_df)


# 关闭数据库连接
conn.close()











































