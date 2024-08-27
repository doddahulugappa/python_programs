import matplotlib.pyplot as plt
import numpy as np
from numpy import ma

X=np.arange(0, 2 * np.pi, .2)
Y=np.ones(X.shape)
U= np.cos(X)
V= np.sin(X)
plt.figure()
plt.plot(X,X,'--')
Q = plt.quiver(X, Y, Y, Y, units='width')
Q = plt.quiver(X, Y-2, U, V, units='width')
plt.show()