import numpy as np


"""
concatenate
传入的参数必须是一个多个数组的元组或者列表
另外需要指定拼接的方向，默认是 axis = 0，
"""
x = [[1,2],[3,4]]
a = np.concatenate((x,x),axis=1)


print(a)
"""
extend and append
listwise elementwise
"""
l1 = [1, 1, 1, 2, 2, 3]
l1.append([9, 9, 9])  # treat argument as a element
l1.extend([9, 9, 9, 9, 9])  # treat argument as a sequence
print(l1)



"""
 array()函数中矩阵的乘积只能使用 .dot()函数。而星号乘 （*）则表示矩阵对应位置元素相乘
 mat()函数中矩阵的乘积可以使用（星号） *  或 .dot()函数，其结果相同。而矩阵对应位置元素相乘需调用numpy.multiply()函数
"""
print("-------------------------------------")
a1 = np.array([[1,2,3],[4,5,6]])
a2 = np.array([[1],[1],[1]])
print("shape of a1 : ",a1.shape)
print("shape of a2 : ",a2.shape)
r1 = a1.dot(a2)

# a1 is a array
r2 = a1*a1
print("result elementwise  r2: ",r2)
print(r1)
print("-------------------------------------")
m1 = np.mat([[1,2,3],[4,5,6]])
m2 = np.mat([[1],[1],[1]])

print(m1.shape)
print(m2.shape)

# m1,m2 is matrix
print(m1*m2)
print(m1.dot(m2))
print(np.multiply(m1,m1))
print("------------------------------matrix------------")
m3 = np.mat([1,2,3])
m6 = np.mat([1,2,3],[4,5,6])
m4 = np.mat([[1,4],[1,6],[2,3]])
#print(m3*m3) 矩阵乘法
print(np.multiply(m3.T,m3))
print(np.sum(m4,axis=0))
print(np.sum(m4,axis = 1))
print(np.sum(m4))
print("---")
print(sum(m4))



print(1 - m3.T)#这是什么操作
print(m6)
print(m6.T)













