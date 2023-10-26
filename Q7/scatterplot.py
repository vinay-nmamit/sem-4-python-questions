import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(60)
y = np.random.randn(60)
plt.scatter(x,y, s=70,facecolors='none',edgecolors='blue')
plt.xlabel("x")
plt.ylabel("y")
plt.show()







