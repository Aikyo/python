


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
lst = table.query_tuple_table(conn,"select distinct(no) from material where time >'2019-08-31 14:45:21' and time < '2019-08-31 17:45:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';")

lst = table.query_tuple_table(conn,"select distinct(no) from material where time >'2019-08-30 13:16:21' and time < '2019-08-30 16:16:21' and no not like('%空飞杆循环') and no not like ('%空杆回调') and no not like '%退镀';")


print(lst)
i= 0
writer = pd.ExcelWriter('超时配方_truncat.xlsx')

total = {x:[0,0,0,0,100000,[],[]] for x in range(1,94)}


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
    # 总杆数
    for q in df['slot']:
        total.get(int(q))[0] += 1

    ls1 = [7,9,16,19,26,28,32,37,40,10,11,27,22,23,24,35,25,36,69,67,68,70,]
    ls4 = [13, 14, 15, 86, 87, 88, 89, 90]
    ls2 = [72, 75, 76, 77, 78, 79, 80]
    ls11 = [8, 18, 31, 39]
    df = df.loc[(df['over_time'] > 0) & ( (df['slot'].isin(ls1)) | (df['over_time'] > 300) | ( (df['slot'].isin(ls11))&(df['over_time']>60  ) )  |  (  (df['over_time'] > 120) &(df['slot'].isin(ls2)) )  | ( (df['over_time'] > 240 ) & (df['slot'].isin(ls4)) )  )]
    #
    # for l in df['slot']:
    #     total.get(int(l))[1] += 1
    #     total.get(int(l))[2] = total.get(int(l))[2] + df
    #     total.get(int(l))[3]
    def func(df):
        global total
        i = int(df['slot'])
        total.get(int(df['slot']))[1] += 1
        print(total.get(int(df['slot']))[1])
        total.get(int(df['slot']))[2] = total.get(int(df['slot']))[2] + df['over_time']
        total.get(i)[5].append(df['over_time'])
        total.get(i)[6].append(x)

        total.get(int(df['slot']))[3] = df['over_time'] if df['over_time'] > total.get(int(df['slot']))[3] else total.get(int(df['slot']))[3]
        total.get(int(df['slot']))[4] = df['over_time'] if df['over_time'] < total.get(int(df['slot']))[4] else total.get(int(df['slot']))[4]
    df.apply(func,axis =1)


    df[x[0]] = [0] * len(df['slot'])
    # print(df)
    df.to_excel(writer, startcol = i * 10)
    i += 1
writer.save()

df_total = pd.DataFrame(total,index=['总杆数','超时杆数','超时总数','最大超时时间','最小超时时间','超时列表','配方列表']).T
print(df_total)
df_total['最小超时时间'] = df_total['最小超时时间'].map(lambda x: 0 if x == 100000 else x)
df_total = df_total.loc[df_total['超时总数'] != 0]

df_total['平均超时'] = df_total['超时总数'] / df_total['超时杆数']

slot_name = table.query_tuple_table(conn,"select name from yangji_slot_info")
df_total['slot_name'] = pd.Series(slot_name).shift(1)
# df_total = df_total.loc[df_total['超时总数'] != 0]
df_total = df_total.loc[df_total['最大超时时间'] > 10]
df_total = df_total.loc[df_total['超时杆数'] > 3]
import matplotlib.pyplot as plt
import pylab as mpl
df_total.to_excel('模拟数据画图_.xls')

k=0
def draw(data,slot_list):
    # 画图
    global k
    import matplotlib.pyplot as plt
    import pylab as mpl
    l3 = data['配方列表']
    # l3 = [x[0].split('-')[-1] + str(i) for x in l3]
    l3 = [x[0] for x in l3]
    l1 = data['超时列表']
    s = 0
    for v in l1:
        s = s + v
    mean = s/len(l1)
    l4 = [mean] * len(l1)
    print(l3, l1)
    plt.bar(l3, l1, width=0.5)
    # plt.plot(l3,l4)
    # plt.show()
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title(data['slot_name'][0]+str(slot_list[k]))
    for a, b in zip(l3, l1):
        plt.text(a, b + 0.001, '%d' % b, ha='center', va='bottom', fontsize=9)
    plt.savefig("./moni2/%s.jpeg" % str(slot_list[k]))
    k+=1
    plt.cla()

df_total.apply(draw,slot_list=df_total.index,axis = 1)
df_total.to_excel('模拟数据_choshi_truncat2.xls')
























