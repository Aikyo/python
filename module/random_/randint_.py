#产生四个随机数
"""
random.randint()
random.random()
random.shuffle() shuffle a list return none


"""
import random
s = set()
while len(s)<4:
    s.add(random.randint(0,10))

lst1 = [1,2,3,4,5,6]
random.shuffle(lst1)



print("shuffle :",lst1)

print(s)
lst = [1,2,3,4,5,6,7,8,9,10]

print([lst[i] for i in list(s)])

