import os
base = os.path.dirname(__file__)
print(base)
b1 = os.path.join(base,'a.py')
print(b1)



with open('../static/herman') as f:
    for l in f.readlines():
        print(l)






