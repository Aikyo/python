

from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse


table = TableOperation()
conn = table.get_py_connect()




name = '思科面板'
table = TableOperation()
conn = table.get_py_connect()
sql = 'select formula_id,name from formula where name = \'{}\' '.format(name)
formula = table.query_table(conn, sql)
print(formula)

sql1 = 'select slot from formula_{};'.format(formula[0]['formula_id'])
slot_list = table.query_table(conn, sql1)
print(slot_list)