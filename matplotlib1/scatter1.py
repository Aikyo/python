"""
scatter(x,y,c='r',marker='o')

"""


import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("LR-testSet.csv",delimiter=',')
x_data = data[:,:-1]
y_data = data[:,-1]


def plot(x_data, y_data):
    x0 = []
    y0 = []
    x1 = []
    y1 = []
    for i in range(0, len(x_data)):
        if y_data[i] == 0:
            x0.append(x_data[i, 0])
            y0.append(x_data[i, 1])
        else:
            x1.append(x_data[i, 0])
            y1.append(x_data[i, 1])
    scatter0 = plt.scatter(x0, y0, marker='o')
    scatter1 = plt.scatter(x1, y1, marker='x')
    plt.legend(handles=[scatter0, scatter1], labels=['label0', 'label1'], loc='best')


plot(x_data, y_data)
plt.show()
