

sql = "select distinct(no),time from material where time >'2019-09-05 16:46:46' and time < '2019-09-05 19:46:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"

# sql = "select distinct(no),time from material where time >'2019-09-05 20:48:46' and time < '2019-09-05 23:48:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"

# sql = "select distinct(no),time from material where time >'2019-09-05 20:48:46' and time < '2019-09-05 23:48:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"


# sql = "select distinct(no),time from material where time >'2019-09-06 08:48:46' and time < '2019-09-06 11:48:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"


sql = "select distinct(no),time from material where time >'2019-08-31 14:45:21' and time < '2019-08-31 17:45:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';"




# sql = "select DISTINCT(no),time from process where time >'2019-09-05 16:46:46' and time < '2019-09-05 19:46:21' and slot in (91,92,93) "
# sql = "select DISTINCT(no),time from process where time >'2019-09-05 20:48:46' and time < '2019-09-05 23:48:21' and slot in (91,92,93) "
# sql = "select DISTINCT(no),time from process where time >'2019-09-06 08:48:46' and time < '2019-09-06 11:48:21' and slot in (91,92,93) and no is not null and no  not like '%退镀'"

sql = "select no,MIN(time) time from process  where time >'2019-09-05 16:46:46' and time < '2019-09-05 19:46:21' and slot in (91,92,93) and no is not null and no  not like '%退镀' and no not like '%回调' and no not like('%空飞杆循环') GROUP BY no"
#
# sql = "select no,MIN(time) time from process  where time >'2019-09-05 20:48:46' and time < '2019-09-05 23:48:21' and slot in (91,92,93) and no is not null and no  not like '%退镀' and no not like '%回调' and no not like('%空飞杆循环') GROUP BY no"
#
# sql = "select no,MIN(time) time from process  where time >'2019-09-06 08:48:46' and time < '2019-09-06 11:48:21' and slot in (91,92,93) and no is not null and no  not like '%退镀' and no not like '%回调' and no not like('%空飞杆循环') GROUP BY no"



name = '0905_1'



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

import matplotlib.pyplot as plt
import pylab as mpl
l3 = df['no']
index = [i for i in range(len(l3))]
# l3 = [x[0].split('-')[-1] + str(i) for x in l3]
# l3 = [x[0] for x in l3]
l1 = df['interval']
mean = df['interval'].mean()
l_mean = [mean] * len(l3)
print(l3, l1)
print(mean)
plt.plot(index,l_mean,label='mean-' + str(round(mean)),c='g')
plt.bar(index, l1, width=0.5)
# plt.show()
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
plt.title('下料interval')
plt.legend()
for a, b in zip(index, l1):
    plt.text(a, b + 0.001, '%d' % b, ha='center', va='bottom', fontsize=9)
plt.savefig("./0906_xl/%s.jpeg" % name)

























