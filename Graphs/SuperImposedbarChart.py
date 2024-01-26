import random

import numpy as np
from matplotlib import pyplot as plt

a = [random.randint(1, 10) for i in range(9)]
b = [random.randint(5, 15) for i in range(9)]
ind = np.arange(len(a))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(x=ind, height=a, width=0.35, align='center', label="a")
ax.bar(x=ind, height=b, width=0.35 / 3, align='center', label="b")

plt.xticks(ind, a)
plt.legend()

plt.tight_layout()
plt.show()
