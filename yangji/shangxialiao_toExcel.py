from Table.yangji import TableOperation
import pandas as pd



table = TableOperation()
#sql = "SELECT * FROM yangji.process limit 10;"
daily_sql = """
SELECT time as 时间 , f.name as 类型, slot as 槽位, quantity as 数量 
from yangji.material, yangji.process ,yangji.formula f
where material.no = process.no and material.formula_id = f.formula_id 
and slot in (91,92) 
and material.time > '2019-01-14 00:00:00.000000' order by time asc;

"""
overtime_sql = """
select slot_name ,slot, avg(overtime) as avg_overtime,sum(overtime) as sum_overtime  
from (select slot_name, slot,process_time - standard_time as overtime from yangji.process) t group by t.slot order by slot;

"""

conn = table.get_py_connect()

df = pd.read_sql(overtime_sql,conn)
df.to_excel('daily_overtime.xls')
#data = table.query_table(conn,sql)
conn.close()
#print(data)


