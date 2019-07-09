from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse


table = TableOperation()
conn = table.get_py_connect()

sql = 'select formula_id,name from formula'
formula_list = table.query_table(conn,sql)

slot = 1
formulas = []
for f in formula_list:
    sql1 = 'select slot from formula_{} limit 1;'.format(f['formula_id'])

    data = table.query_tuple_table(conn,sql1)
    # print(data)
    # print("------",data[0][0],type(data[0][0]))
    #
    if str(slot) in data[0][0].split(','):

        formulas.append(f['name'])


print('--------')
print(formulas)












