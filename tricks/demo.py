import sklearn
import numpy as np
import matplotlib.pyplot as plt

def pyplot():
    x = np.linspace(-1, 1, 100)
    y = x ** 2
    noise = np.random.normal(0, 0.05, 100)
    plt.plot(x, y + noise)
    plt.show()