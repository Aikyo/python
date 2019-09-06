
from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse

from anode_pole.util import fast_generate_chart

def get_table_name(table, conn, name):
    sql = 'select formula_id from formula where name=\'{}\''.format(name)
    query_data = table.query_table(conn, sql)
    if query_data:
        table_name = 'formula_' + query_data[0].get('formula_id')
        return table_name


table = TableOperation()
conn = table.get_py_connect()

sql = """select crane,slot,slot_name,type,time,standard_time,extra_time,manual,max_time from process
where time >'2019-08-31 16:45:21' and time < '2019-08-31 16:55:21';"""

sql = """select crane,slot,slot_name,type,time,standard_time,extra_time,manual,max_time from process
where no = '20190831154057-2016-便当盒验证';"""

sql = """select crane,slot,slot_name,type,time,standard_time,extra_time,manual,max_time from process
where time >'2019-08-31 16:45:21' and time < '2019-08-31 16:55:21';"""


# sql = """select no,time from process
# where time >'2019-08-31 16:45:21' and time < '2019-08-31 16:50:21';"""
# "crane","slot","slot_name","type","time","standard_time","extra_time","manual","max_time"

def func1(df):
    df
    result = fast_generate_chart(df)
    df = pd.DataFrame(result[0], columns=result[1])
    return df

import numpy as np
import time
data = pd.read_sql(sql,conn)
data = data.groupby(['no']).apply(func1)
# data = list(data)
for x in data:
    t = x['time'].timetuple()
    x['time'] = np.float(time.mktime(t))

result=fast_generate_chart(data)

