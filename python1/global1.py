"""
global 局部变量变成全局变量

"""
a = 1
def ch():
    global a
    a = 0
    print(" a = ",a)

ch()
print(" a = ",a)