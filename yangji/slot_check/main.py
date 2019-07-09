
from Table.yangji import TableOperation
import pandas as pd
from dateutil.parser import parse


table = TableOperation()
conn = table.get_py_connect()
sql = 'select formula_id,name from formula where name = \'{}\' '.format('')
formula = table.query_table(conn, sql)
sql1 = 'select slot from formula_{};'.format(formula[0]['formula_id'])
slot_list = table.query_table(conn, sql1)
closed = []
for i in slot_list:
    slots = i['slot'].split(',')
    for slot in slots:
        slot_ = []
        if global_data[GROUP_NAME_PREFIX + 'Slot%sInUse' % slot]:
            break
        else:
            slot_.append(slot)
        closed.append(slot_)