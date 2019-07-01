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
    for index,row1 in formula.iterrows():
        threshold = row1['standard_time'] / len(row1['slot'].split(','))
        lst.append(threshold)
    formula['瓶颈时间'] = lst
    formula.to_excel( row['name']+ '.xls')
conn.close()