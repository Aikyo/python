import random
import numpy as np
print(random.random())
print(random.uniform(12,23))
print(random.choice(['win', 'lose', 'draw']))
deck = 'ace two three four'.split()
strr = 'i,am,kiko'.split(',')
print(strr)
print(deck)
random.shuffle(deck)
print(deck)
print("---------------------")
print("生成一个随机数：",np.random.random())
print("生成指定数量的随机数 :",np.random.random(10))
print("生成随机数矩阵 ：",np.random.random_sample((2,3)))
print("生成整数随机数",np.random.randint(3,8,5))
print("生成高斯分布的随机数",np.random.normal(5,0.5,6))# loc=u scala=variance size=size
print("---------------------------------------------")

"""
seed( ) 用于指定随机数生成时所用算法开始的整数值，如果使用相同的seed( )值，则每次生成的随即数都相同
，如果不设置这个值，则系统根据时间来自己选择这个值，此时每次生成的随机数因时间差异而不同。
"""
np.random.seed(1)
print(np.random.random())
np.random.seed(1)
print(np.random.random())
