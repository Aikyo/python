
from sqlalchemy import create_engine
engine=create_engine('mysql+pymysql://root:123456@localhost:3306/yangji', echo=True) #echo=True 打印sql语句信息

# db_info = {'user': self.user, 'password': self.password, 'host': self.host, 'port': self.port, 'db': self.db}
# engine = create_engine("mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(**db_info))
connect = engine.connect()
import pandas as pd
import numpy as np
import json
df = pd.DataFrame(data=np.random.normal(1,0.5,9).reshape([3,-1]),columns=list('abc'))
print(df)
df.to_sql('hey_test', con=connect, if_exists='replace')


data = json.loads('[{"index":1,"slot":"93","standard_time":1,"max_time":1,"load_module":"","load_value":""},{"index":2,"slot":"55","standard_time":1,"max_time":1,"load_module":"","load_value":"1"}]')
from sqlalchemy import Integer, NVARCHAR, Float
# 配方类型
dtype_dict = {
            'index': Integer(),
            'standard_time': Integer(),
            'max_time': Integer(),
            'slot': NVARCHAR(50),
            'load_module': NVARCHAR(30),
            'load_value': Float()
        }

d1 = pd.DataFrame(data)
d1.fillna(value=0,inplace=True)
print(d1)
print('----------------------------')
d1['index'] = range(1, len(d1) + 1)
d1['load_value'] = d1['load_value'].replace(to_replace='',value='0')
# d1.drop(columns=['load_value'],inplace=True)
d1.to_sql('formula_test',connect,if_exists='replace',dtype=dtype_dict,index=False)






