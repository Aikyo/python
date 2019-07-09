from Table.yangji import TableOperation
import pandas as pd

table = TableOperation()
conn = table.get_py_connect()

formula_list = """select name,formula_id from formula"""

formulas = pd.read_sql(formula_list,conn)
writer = pd.ExcelWriter('瓶颈时间汇总.xlsx')
#a = 0
for i,(index,row) in enumerate(formulas.iterrows()):
    sheetname = row['name']
    print('index index ---',index)
    sql = "select standard_time,slot from {} ".format("formula_" + row['formula_id'])
    print(sql)
    formula = pd.read_sql(sql,conn)
    lst = []
    for index,row1 in formula.iterrows():
        threshold = row1['standard_time'] / len(row1['slot'].split(','))
        lst.append(threshold)
    formula['瓶颈时间'] = lst

    formula.insert(3,row['name'],[x*0 for x in lst])
    #formula.to_excel( row['name']+ '.xls')
    print(len(lst))
    print(type(formula))

    formula.to_excel(writer,startcol=i*10)

writer.save()
writer.close()
conn.close()