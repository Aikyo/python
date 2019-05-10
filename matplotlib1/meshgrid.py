import numpy as np
import matplotlib.pyplot as plt

x,y = np.arange(1,12,0.5),np.arange(1,13,0.8)
xx,yy = np.meshgrid(x,y)
print(x)
print("---------------------")
print(xx)
plt.scatter(xx,yy,c='r',marker='x')
plt.show()