import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5)
y1 = [5, 25, 15, 20, 10]
y2 = [10, 20, 30, 45, 50]

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(x, y1)
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')
ax2.set_ylabel('Y2 data', color='b')
plt.legend()
plt.show()
