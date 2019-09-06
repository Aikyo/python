
from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse


def get_table_name(table, conn, name):
    sql = 'select formula_id from formula where name=\'{}\''.format(name)
    query_data = table.query_table(conn, sql)
    if query_data:
        table_name = 'formula_' + query_data[0].get('formula_id')
        return table_name


table = TableOperation()
conn = table.get_py_connect()

table = TableOperation()
conn = table.get_py_connect()
table_name = get_table_name(table, conn, '便当盒')
sql_slot = 'select slot from {}'.format(table_name)
# formula_slot = table.query_tuple_table(conn, sql_slot)
formula_slot = table.query_tuple_table(conn, sql_slot)
formula_no_list = []
for fs in formula_slot:
    no_list = list(map(int, fs[0].split(',')))
    formula_no_list.append({'no': fs[0], 'name': slots_info().get(no_list[0])})
conn.close()










