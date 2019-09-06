
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
# lst = table.query_tuple_table(conn,"select distinct(no) from process where time >'2019-08-31 16:45:21' and time < '2019-08-31 17:45:21'")
lst = table.query_tuple_table(conn,"select distinct(no) from material where time >'2019-08-31 14:45:21' and time < '2019-08-31 17:45:21' and no not like('%空飞杆循环') and no not like ('%空杆回调');")

print(lst)
i= 0
writer = pd.ExcelWriter('超时时间.xlsx')
le = len(lst)
print(len(lst))



for x in lst:
    sql = """select crane,slot,slot_name,type,time,standard_time,extra_time,manual,max_time from process
    where no = '{}';""".format(x[0])
    print(sql)
    import numpy as np
    import time
    data = table.query_table(conn,sql)
    # data = data.apply(func1)
    # data = list(data)
    for l in data:
        t = l['time'].timetuple()
        l['time'] = np.float(time.mktime(t))

    result=fast_generate_chart(data)
    # result = fast_generate_chart(df)
    df = pd.DataFrame(result[0], columns=result[1])
    df = df[['slot','slot_name','process_time','standard_time']]
    df['over_time'] = df['process_time'] - df['standard_time']

    ls1 = [7,9,16,19,26,28,32,37,40,10,11,27,22,23,24,35,25,36,69,67,68,70,]
    ls4 = [13, 14, 15, 86, 87, 88, 89, 90]
    ls2 = [72, 75, 76, 77, 78, 79, 80]
    ls11 = [8, 18, 31, 39]
    df = df.loc[(df['over_time'] > 0) & ( (df['slot'].isin(ls1)) | (df['over_time'] > 300) | ( (df['slot'].isin(ls11))&(df['over_time']>60  ) )  |  (  (df['over_time'] > 120) &(df['slot'].isin(ls2)) )  | ( (df['over_time'] > 240 ) & (df['slot'].isin(ls4)) )  )]
    # df = df.loc[(df['slot'].isin(ls1)) | (df['over_time'] > 60 & df['slot'].isin(ls11)) | df['over_time'] > 300]


    # df = df.loc[(df['over_time']>0) & (        ( df['slot'].isin(ls1) ) | (    (df['over_time'] >60) & ( df['slot'].isin(ls11)) )    |    ( (df['over_time']>120) &(df['slot'].isin(ls2))) | ( (df['over_time']>240)&(df['slot'].isin(ls4)) ) | df['over_time'] > 300)]
    #
    # df = df.loc[(df['over_time'] > 0) & ((df['slot'].isin(ls1)) | ((df['over_time'] > 60) & (df['slot'].isin(ls11))) | (
    #             (df['over_time'] > 120) & (df['slot'].isin(ls2))) | ((df['over_time'] > 240) & (df['slot'].isin(ls4))) |
    #                                      df['over_time'] > 300)]

    # df = df.loc[(df['over_time'] > 60 | (df['over_time'].isin([])))]
    df[x[0]] = [0] * len(df['slot'])
    print(df)
    df.to_excel(writer, startcol = i * 10)
    i += 1

writer.save()
writer.close()
conn.close()



