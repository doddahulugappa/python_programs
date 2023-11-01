# libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dataset
df = pd.DataFrame(np.random.random((10, 10)), columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])

# plot using a color palette
sns.heatmap(df, cmap="YlGnBu")
plt.show()

sns.heatmap(df, cmap="Blues")
plt.show()

sns.heatmap(df, cmap="BuPu")
plt.show()

sns.heatmap(df, cmap="Greens")
plt.show()

# plot heatmap
sns.heatmap(df, cmap="PiYG")
plt.show()

# plot heatmap
sns.heatmap(df, center=1)
plt.show()

# color bar range between 0 and 0.5
sns.heatmap(df, vmin=0, vmax=0.5)
plt.show()


