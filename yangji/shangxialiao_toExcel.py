from Table.yangji import TableOperation
import pandas as pd

table = TableOperation()
#sql = "SELECT * FROM yangji.process limit 10;"
daily_sql = """
SELECT time as 时间 ,name as 类型, slot as 槽位, quantity as 数量 
from yangji.material, yangji.process 
where material.no = process.no 
and slot in (91,92) 
and material.time > '2019-06-26 00:00:00.000000' order by time asc;

"""

daily_sql2 = """
select time as 时间,name as 类型,quantity as 数量,slot as 槽位 
from material m LEFT JOIN process p on m.NO = p.NO 
where slot in (91,92) and time > '2019-06-26 00:00:00.000000'
ORDER BY time asc;

"""


overtime_sql = """
select slot_name ,slot, avg(overtime) as avg_overtime,sum(overtime) as sum_overtime  
from (select slot_name, slot,process_time - standard_time as overtime from yangji.process 
where in_slot_time is not null and out_slot_time is not null and in_slot_time > '2019-01-14 00:00:00.000000') t 
group by t.slot order by slot;

"""

overtime_sql2 = """
SELECT slot,slot_name,sum(overtime) as total_overtime,avg(overtime) as average_overtime from 
(select slot,slot_name,(process_time-standard_time) overtime from process 
where in_slot_time is not null and out_slot_time is not null and in_slot_time > '2019-06-26 00:00:00.000000'
) t 
GROUP BY t.slot
ORDER BY t.slot
"""

conn = table.get_py_connect()

df = pd.read_sql(overtime_sql2,conn)
df.to_excel('0626_overtime.xls')
#data = table.query_table(conn,sql)
conn.close()
#print(data)


