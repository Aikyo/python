
import pandas as pd
from Table.yangji import TableOperation


table = TableOperation()
#连接数据库
conn = table.get_py_connect()
#获取数据

import datetime

start_time = datetime.date(year=2019, month=4, day=11)
end_time = start_time + datetime.timedelta(days=1)
# start_time = datetime.datetime.now().date()
#     # end_time = start_time + datetime.timedelta(days=1)
table = TableOperation()
conn = table.get_py_connect()
sql = 'SELECT material.no, material.name, material.time, material.quantity from material, process ' \
      'where material.no = process.no and material.time > \'%s\' and material.time < \'%s\' ' \
      'group by material.`no` having MAX(process.id) in (SELECT id from process ' \
      'where slot in (91,92,93)) and count(process.id) > 1' % (start_time.isoformat(), end_time.isoformat())
df = pd.read_sql(sql, conn)
# 关闭数据库连接
conn.close()
p = pd.date_range(start=start_time, end=end_time, freq='2H')
print(p)
print('-------------------------')
freq_list = []
for name, df in df.groupby('name'):
    n_df = pd.cut(df.time, p)


    #new_df = (pd.concat([n_df, df.loc[n_df.index, 'quantity']], axis=1)) # 花里胡哨的
    new_df = pd.concat([n_df,df['quantity']],axis=1)
    quantity_sum = new_df.groupby('time')['quantity'].sum()
    quantity_sum.name = name
    freq_list.append(quantity_sum)
print(freq_list[1])
print(type(freq_list[1]))
print('=========================')
if freq_list:
    freq_df = pd.concat(freq_list, axis=1)
    print('=================')
    print(freq_df.index)
    print(type(freq_df.index))
    print('=======================')
    freq_df.index = freq_df.index.map(lambda o: o.left.strftime('%H:%M:%S'))

print(freq_df)