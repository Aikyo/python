from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse


table = TableOperation()
conn = table.get_py_connect()

sql_process = """select slot,slot_name operate_type,in_slot_time time from process 
where in_slot_time is not null  and in_slot_time > '2019-06-28 00:00:00.000000' and slot in (1,2,3) order by slot,time """
sql_operate_log  = """ select * from operate_log 
where operate_type = '上料操作' and add_time > '2019-06-28 00:00:00.000000' and content like '上料%' 
order by add_time
 """

data_process = pd.read_sql(sql_process,conn)
data_operate_log = pd.read_sql(sql_operate_log,conn)
print(data_process.head())
import re
lst = []
for index,row in data_operate_log.iterrows():
    result = re.findall('\d#',row['content'])
    lst.append(int(result[0][0]))
log = data_operate_log[['operate_type','add_time']]
log.insert(0,'slot',lst)
log = log.rename(columns = {'add_time':'time'})
print(log.head())
print("dataprocess length " , len(data_process))
print(" log length        " , len(log))
data = pd.concat([log,data_process])
print(" concat length ",len(data))
data = data.sort_values(by = ['slot','time'],)
print(data)
data.to_excel('0628_上下挂与上料.xls')

total = {'1':0,'2':0,'3':0}
temp = {}
for index,row in data.iterrows():
    #temp = {}

    x = temp.get(row['slot'])
    #print(index)
    print("slot",row['slot'])
    print(index, " type",row['operate_type'])

    if not x:
        if row['operate_type'] == '上下挂':
            temp[row['slot']] = [row['operate_type'],row['time']]
            continue
        else:
            continue
    if x[0] == row['operate_type']:
        x[1] = row['time']
    else:
        print(row['time'])
        delta = (parse(str(row['time'])) - parse(str(x[1]))).total_seconds()
        print('时间差',delta)
        if delta > 3600:
            total[str(row['slot'])] += delta-3600
print(total)
for i in range(1,4):
    print(total[str(i)] / 60)





