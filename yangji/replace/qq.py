from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse
import pandas as pd

table = TableOperation()
connect = table.get_sql_connect()
conn = table.get_py_connect()
data_list = [{'id':12,'alarm_id':'PLC.Alarm42','content':'ddd'}]
sql = 'select * from yangji_alarm_black_list'
data = table.query_tuple_table(connect,sql)
print(data)


table.replace_not_reset(connect, 'yangji_alarm_black_list', data_list)



import numpy as np
array = np.random.normal(5,1,9).reshape([3,-1])
df = pd.DataFrame(array,columns=list('abc'))


# df = pd.DataFrame(pd.Series(data[0]),columns=['no','id','content'],index= [1])
print(df)
df.to_sql('herman', con=connect, if_exists='replace', index_label='id')












