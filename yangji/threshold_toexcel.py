from Table.yangji import TableOperation
import pandas as pd

table = TableOperation()
conn = table.get_py_connect()

formula_list = """select name,formula_id from formula"""

formulas = pd.read_sql(formula_list,conn)
#writer = pd.ExcelWriter('配方各槽位瓶颈时间.xlsx')
#a = 0
for index,row in formulas.iterrows():
    sheetname = row['name']

    sql = "select standard_time,slot from {} ".format("formula_" + row['formula_id'])
    print(sql)
    formula = pd.read_sql(sql,conn)
    lst = []
    lst2 = []
    lst3 = []
    for index,row in formula.iterrows():


        threshold = row['standard_time']/len(row['slot'].split(','))
        lst.append(threshold)
        lst2.append(len(row['slot'].split(',')))
        lst3.append(row['standard_time'])
        # print("--",row['slot'])
        # print("--", row['slot'].split(','))
        # print("--", len(row['slot'].split(',')))


    result = formula[['slot','standard_time']]
    print("-------------" , len(lst))
    print(lst)
    print(lst2)
    print(lst3)
    print(len(formula['slot']))

    #formula['threshold'] = lst
    #result['threshold'] = lst
    print(row['name'])
    result.to_excel('dd.xls')







