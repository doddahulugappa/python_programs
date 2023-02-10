import matplotlib.pyplot as plt
import numpy as np

# Enfield:
x = np.array([1, 2, 3, 4, 5, ])
y = np.array([50, 40, 70, 80, 20])
color = "red"
bike = "Enfield"
plt.scatter(x, y, c=color, marker="o", label=bike)

# Yamaha:
x = np.array([1, 2, 3, 4, 5])
y = np.array([70, 21, 61, 41, 60])
color = "green"
bike = "Yamaha"
plt.scatter(x, y, c=color, marker="P", label=bike)

# KTM:
x = np.array([1, 2, 3, 4, 5])
y = np.array([60, 30, 50, 60, 70])
color = "black"
bike = "KTM"
plt.scatter(x, y, c=color, marker="s", label=bike)

plt.ylabel("Distance in kms")
plt.xlabel("Days")
plt.suptitle("Bike details in Scatter Plot")  # title of the graph
plt.legend()  # adds legend
plt.show()  # shows the plot
