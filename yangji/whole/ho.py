


import pandas as pd
from Table.yangji import TableOperation


table = TableOperation()
#连接数据库
conn = table.get_py_connect()
table = TableOperation()
conn = table.get_py_connect()
sql = 'select distinct name from material'
data_tuple = table.query_tuple_table(conn, sql)
conn.close()
data_list = []
for data in data_tuple:
    data_list.append(data[0])

print(data_list)
print(len(data_list))


















