from Table.yangji import TableOperation
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import pylab as mpl

table = TableOperation()
conn = table.get_py_connect()

formula_list = """select name,formula_id from formula"""

formulas = pd.read_sql(formula_list,conn)
writer = pd.ExcelWriter('0711formulas0.xlsx')
total_time = []
formula_time_map = {}#寄存
for l,(index4,row) in enumerate(formulas.iterrows()):
    data = {
        '天车': ['A', 'B', 'C', 'D', 'E', 'H', 'I', 'J', 'K'],
        '工作区间': ['1-16', '16-20', '20-37', '37-43', '43-55', '55-61', '61-77', '77-84', '84-93'],
        # '工作时间':[84,]
    }
    data = pd.DataFrame(data)
    sheetname = row['name']
    sql = "select standard_time,slot from {} ".format("formula_" + row['formula_id'])
    formula = pd.read_sql(sql,conn)
    lst = []
    lst1 = []
    for index,row1 in formula.iterrows():
        # for i in row1['slot'].split(','):
        #     lst1.append(int(i))
        lst1.append(row1['slot'])
        k = row1['slot'].split(',')[-1]
        lst.append(int(k))
    print(row['name'])
    print(lst)
    print(lst1)
    print(len(lst))
    #print(lst1)
    print('herman')

    lst2 = pd.cut(lst,[0,16,20,37,43,55,61,77,84,93],labels=['A','B','C','D','E', 'H','I','J','K']).tolist()
    print(lst2)

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
    print(data)
    data['上下时间'] = lst3
    for index4,row4 in data.iterrows():
        #if lst3[index4] != 0 or (lst3[0] !=0 and lst3[-1] != 0):#等于o这个天车在这个区间没有工作
        if lst3[index4] != 0 or (lst3[3] != 0 and lst3[4] != 0):
            t = row4['工作区间'].split('-')
            steps = abs(int(t[0]) - int(t[1]))
           # print(row4['工作时间'])
            #row4['工作时间'] += steps*6
            if row4['天车'] not in ('A','K'):
                lst3[index4] -= 10
            lst3[index4] = lst3[index4] + steps*6

       # print(row4['工作时间'])

    data['工作时间'] = lst3
    data.insert(3, row['name'], [x * 0 for x in lst3])

    #print(data)

    total_time.append(data['工作时间'].sum())
    formula_time_map[row['formula_id']] = data


    #画图
    plt.bar(data['天车'],data['工作时间'])
    #plt.show()
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title(row['name'])
    for a, b in zip(data['天车'], data['工作时间']):
        plt.text(a, b + 0.001, '%d' % b, ha='center', va='bottom', fontsize=9)
    plt.savefig("./tupian/%s.png"%row['name'])
    plt.cla()

    #统计表格
    data.to_excel(writer , startcol= int(l) * 8)


total = pd.DataFrame({'total_time':total_time})
total['formula'] = formulas['name']
total['formula_id'] = formulas['formula_id']



sql3 = """
select formula_id,name,count(1) quantity_
from (SELECT material.no,material.formula_id, material.name, material.time, material.quantity from material, process 
where material.no = process.no and  material.time > '2019-06-11 00:00:00.000000'
group by material.`no` having MAX(process.id) in (SELECT id from process 
where slot in (91,92,93)) and count(process.id) > 1) t
GROUP BY formula_id
"""
#各个配方加工个数

formula_amount = pd.read_sql(sql3,conn)
lst_m = []
print(formula_amount.sort_values(by=['quantity_'],ascending=False))
total_crane = {'A':0,'B':0,'C':0,'D':0,'E':0,'H':0,'I':0,'J':0,'K':0}
for k,v in formula_amount.iterrows():
    d = formula_time_map.get(v['formula_id'],None)
    if d is not None:
        for it,vl in d.iterrows():
            total_crane[vl['天车']] += v['quantity_'] * vl['工作时间']


#画图
l1 = list(total_crane.keys())
l2 = list(total_crane.values())
#print(total_crane.values())
plt.bar(l1,l2)
#plt.show()
mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False
#
for a, b in zip(l1, l2):
    plt.text(a, b + 0.001, '%d' % b, ha='center', va='bottom', fontsize=19)
plt.savefig("./tupian1/%s.png"%('天车汇总'))
plt.cla()



mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False

# for i in range(0,8):
#     start = i * 4
#     end = start + 4
#     plt.bar(total.loc[start:end]['formula'],total.loc[start:end]['summation'])
#     plt.savefig("./summation/%s.png"%('summation' + str(i)))
#     plt.cla()
#


total.to_excel('gg.xls')
writer.save()
writer.close()
conn.close()