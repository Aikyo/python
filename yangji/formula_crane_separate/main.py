from Table.yangji import TableOperation
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pylab as mpl

table = TableOperation()
conn = table.get_py_connect()

formula_list = """select name,formula_id from formula"""

formulas = pd.read_sql(formula_list,conn)
writer = pd.ExcelWriter('formula_crane_separate1111.xlsx')
total_time = []
ttime = {}#寄存
for l,(index4,row) in enumerate(formulas.iterrows()):
    data = {
        '天车': ['A', 'B', 'C', 'D', 'E', 'H', 'I', 'J', 'K'],
        '工作区间': ['1-15', '15-20', '20-32', '32-43', '43-55', '55-61', '61-77', '77-84', '84-93'],
        # '工作时间':[84,]
    }
    data = pd.DataFrame(data)
    sheetname = row['name']


    sql = "select standard_time,slot from {} ".format("formula_" + row['formula_id'])

    formula = pd.read_sql(sql,conn)
    lst = []
    for index,row1 in formula.iterrows():
        for i in row1['slot'].split(','):
            lst.append(int(i))
    lst2 = pd.cut(lst,[0,15,20,32,41,55,66,77,84,93],labels=['A','B','C','D','E', 'H','I','J','K']).tolist()
    test = pd.DataFrame({'slot':lst,'天车':lst2})


    total_step = 0


    lst3 = []
    for crane in data['天车']:

        test1 = test[test['天车'].isin([crane])]


        lst3.append(len(test1)*20)
    #data['工作时间'] = lst3

    # if row['name'] == '带料退镀':
    #     print(test1)
    #     print(lst3)
    #     break
    for index4,row4 in data.iterrows():

        if lst3[index4] != 0:
            t = row4['工作区间'].split('-')
            steps = abs(int(t[0]) - int(t[1]))
           # print(row4['工作时间'])
            #row4['工作时间'] += steps*6
            lst3[index4] = lst3[index4] + steps*6
       # print(row4['工作时间'])

    data['工作时间'] = lst3

    data.insert(3, row['name'], [x * 0 for x in lst3])

    #print(data)

    total_time.append(data['工作时间'].sum())
    ttime[row['formula_id']] = data


    #画图
    # plt.bar(data['天车'],data['工作时间'])
    # #plt.show()
    # mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    # mpl.rcParams['axes.unicode_minus'] = False
    # plt.title(row['name'])
    # for a, b in zip(data['天车'], data['工作时间']):
    #     plt.text(a, b + 0.001, '%d' % b, ha='center', va='bottom', fontsize=9)
    # plt.savefig("./tupian3/%s.png"%row['name'])
    # plt.cla()

    #统计表格
    #data.to_excel(writer , startcol= int(l) * 6)


total = pd.DataFrame({'total_time':total_time})
total['formula'] = formulas['name']
total['formula_id'] = formulas['formula_id']



sql3 = """
select formula_id,count(1) q
from (SELECT material.no,material.formula_id, material.name, material.time, material.quantity from material, process 
where material.no = process.no and  material.time > '2019-06-09 00:00:00.000000'
group by material.`no` having MAX(process.id) in (SELECT id from process 
where slot in (91,92,93)) and count(process.id) > 1) t
GROUP BY formula_id
"""

t2 = pd.read_sql(sql3,conn)
lst_m = []
total_crane = {'A':0,'B':0,'C':0,'D':0,'E':0,'H':0,'I':0,'J':0,'K':0}

for k,v in t2.iterrows():
    d = ttime.get(v['formula_id'],None)
    print('-------------')
    if d is not None:
        for it,vl in d.iterrows():
            total_crane[vl['天车']] += v['q'] * vl['工作时间']
        print('------------------+++++++++++++++')
        print(total_crane)


#画图
print(total_crane)
print(total_crane.keys())
l1 = list(total_crane.keys())
l2 = list(total_crane.values())
#print(total_crane.values())
plt.bar(l1,l2)
#plt.show()
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
#
for a, b in zip(l1, l2):
    plt.text(a, b + 0.001, '%d' % b, ha='center', va='bottom', fontsize=9)
plt.savefig("./tupian3/%s.png"%('天车汇总'))
plt.cla()


#
# for k,v in total.iterrows():
#     q = t2.loc[t2['formula_id'] == v['formula_id']]
#     print(q['q'].tolist())
#     q = q['q'].tolist()
#
#     x = 0
#     if q:
#         x = q[0]
#     tt = x * v['total_time']
#     lst_m.append(tt)







#total['summation'] = lst_m

print(total)

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False

# for i in range(0,8):
#     start = i * 4
#     end = start + 4
#     plt.bar(total.loc[start:end]['formula'],total.loc[start:end]['summation'])
#     plt.savefig("./summation/%s.png"%('summation' + str(i)))
#     plt.cla()
#


total.to_excel('totalss7788811111111111.xls')
writer.save()
writer.close()
conn.close()