from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse


table = TableOperation()
conn = table.get_py_connect()

connect = table.get_sql_connect()

sql = 'select id,formula_id,name from formula'
formula_list = table.query_table(conn, sql)

print(formula_list)


