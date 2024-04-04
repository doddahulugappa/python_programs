import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

my_list = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5]
my_series = pd.Series(my_list)
labels = ["Data"+str(1) for i in range(1, 6)]
ax = sns.histplot(data=my_series, stat='probability', label=labels)

handles = [plt.Line2D([], [], visible=False) for _ in labels]
labels = [f"{stat}: {val:.2f}" for stat, val in my_series.describe().items()]

ax.legend(
    handles,
    labels,
    loc="best",
    handlelength=0,
)
plt.show()
