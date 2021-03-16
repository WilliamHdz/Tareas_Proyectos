import numpy as np
from numpy import arange,sin,pi
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.01)
y = np.sin(x)

plt.plot(x,y)
plt.show()