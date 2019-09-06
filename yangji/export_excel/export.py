import json
from datetime import datetime
from Table.yangji import TableOperation
import pandas as pd
from io import BytesIO



slots = [(1,2,),(12,)]
# for i in range(94):
#     s = request.POST.get('slots[{}]'.format(i))
#     if s is not None:
#         slots.append(tuple(map(int, s.split(','))))
formula = 'x480'
start_str = "1546272000000"
end_str = "1551283200000"

start_time = datetime.fromtimestamp(float(start_str) / 1000)
end_time = datetime.fromtimestamp(float(end_str) / 1000)
table = TableOperation()
conn = table.get_sql_connect()
sql_template = """
   	SELECT
           material.no as '物料号',
           material.time as '上料时间',
           process.slot as '槽号',
           process.slot_name as '名称',
           process.no as process_no,
           process_time as '实际时间',
           standard_time as '标准时间',
           extra_time as '附加时间'
       FROM
           material,
           process
       WHERE
           material.no = process.no
       AND material.name = '{formula}' AND material.time BETWEEN '{start_time}' AND '{end_time}';
   """
sql = sql_template.format(formula=formula, start_time=start_time, end_time=end_time)
print(sql)
data = pd.read_sql(sql_template.format(formula=formula, start_time=start_time, end_time=end_time), conn)
slot_names = pd.read_sql('select no, name from yangji_slot_info', conn).set_index('no').squeeze()
conn.close()


def make_groups(df, slot_list):
    summary = pd.DataFrame()
    for i, (slots, slot_name) in enumerate(slot_list.items()):
        part_df = df[df['槽号'].isin(slots)]
        summary = summary.append(pd.Series({
            '序号': i + 1, '槽号': str(slots), '槽位名称': slot_name, '标准时间': part_df['标准时间'].max(),
            '附加时间': part_df['附加时间'].max(), '实际时间': part_df['实际时间'].max()
        }), ignore_index=True)
    summary = summary.melt(id_vars=['序号', '槽号', '槽位名称'], var_name='项目', value_name='时间')
    return summary.groupby(['序号', '槽号', '槽位名称', '项目']).first()


table = data.groupby(['物料号', '上料时间']).apply(make_groups, slot_list={v: slot_names[v[0]] for v in slots}).unstack(
    level=[0, 1])
print(type(table))
material_no = list(table.columns.levels[1])
table.columns = table.columns.droplevel([0, 1])
table.sort_index(ascending=[True, True, True, False], inplace=True)


print(table)
table.to_excel('ffff.xls')
output = BytesIO()

ew = pd.ExcelWriter(output, engine='openpyxl')

table.to_excel(ew, startrow=1)
