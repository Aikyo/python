

sql = "select distinct(no),time from material where time >'2019-08-30 13:16:21' and time < '2019-08-30 16:16:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"
sql = "select distinct(no),time from material where time >'2019-09-05 16:46:46' and time < '2019-09-05 19:46:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"

sql = "select distinct(no),time from material where time >'2019-09-05 16:46:46' and time < '2019-09-05 19:46:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"

# sql = "select distinct(no),time from material where time >'2019-09-05 20:48:46' and time < '2019-09-05 23:48:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"

# sql = "select distinct(no),time from material where time >'2019-09-06 08:48:46' and time < '2019-09-06 11:48:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"



#
# tu = 'moni_0906_3'
# interval = 'interval'

tu = 'moni_0906'
interval = 'interval'



from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse

from anode_pole.util import fast_generate_chart
import pandas as pd
table = TableOperation()
conn = table.get_py_connect()

df = pd.read_sql(sql,conn)
l = len(df['time'])
df['shift'] = df['time'].shift(1)
df['interval'] = df['time'] - df['shift']
df['interval'] = df['interval'].apply(lambda x:x.seconds)
df.fillna(value=0,inplace=True)
print(df)
# df.to_excel()
import matplotlib.pyplot as plt
import pylab as mpl
l3 = df['no']
print(len(l3),'-------------------------')
index = [i for i in range(len(l3))]
# l3 = [x[0].split('-')[-1] + str(i) for x in l3]
# l3 = [x[0] for x in l3]
l1 = df['interval']
mean = df['interval'].mean()
l_mean = [mean] * len(l3)
# print(l3, l1)
# print(mean)
plt.plot(index,l_mean,label='mean-' + str(round(mean)),c='g')
plt.bar(index, l1, width=0.5)
# plt.show()
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
plt.title('interval')
plt.legend()
for a, b in zip(index, l1):
    plt.text(a, b + 0.001, '%d' % b, ha='center', va='bottom', fontsize=9)

plt.savefig("./%s/%s.jpeg" % (tu,'interval'))

























