
import os
pid = os.getpid()
print(pid)
cmd = "tasklist | findstr {}".format(pid)
result = os.popen(cmd).read()
lst = result.split()
print(result)



print("-----------------")


if not os.path.exists('./herman.xls'):
    os.makedirs('data')