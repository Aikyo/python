import numpy as np

a1 = np.array([1,2,3])

r1 = a1*a1
print(r1)

r2 = np.dot(a1,a1.T)
r3 = a1.dot(a1.T)
print('r3 =  ',r3)
print('r2 =  ',r2)


a2 = np.array([1,2,3])

r5 = a2.dot(a2.T)
r6 = np.dot(a2,a2.T)
print("--------------")
print(r5)

print(r6)