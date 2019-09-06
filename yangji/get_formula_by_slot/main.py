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

print('-----------------------------------------------------------------')

table = TableOperation()
conn = table.get_py_connect()
sql = 'select id,formula_id,name from formula'
formula_list = table.query_table(conn, sql)
slot =  91
formulas = {}
print(formula_list)

print(formula_list[0]['id'])
print(type(formula_list[0]))
for f in formula_list:
    sql1 = 'select slot from formula_{} limit 1;'.format(f['formula_id'])
    data = table.query_tuple_table(conn, sql1)
    if str(slot) in data[0][0].split(','):
        #formulas.app(f['name'])
        formulas[f.get('id',0)] = f['name']
ret = {}
if int(slot) in (91,92,93,):
    formulas['62'] = '空飞杆运行'
ret['code'] = 0
ret['data'] = formulas








