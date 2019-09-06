from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse
import pandas as pd

table = TableOperation()
connect = table.get_sql_connect()
conn = table.get_py_connect()
# sql = 'select * from yangji_alarm_black_list'
# data = table.query_tuple_table(conn,sql)
# print(data)

data_list = [{'id':12,'alarm_id':'PLC.Alarm42','content':'ddd'}]


table.replace_not_reset(connect, 'yangji_alarm_black_list', data_list)









