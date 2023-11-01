import seaborn as sns
import matplotlib.pyplot as plt


df = sns.load_dataset("titanic")
sns.violinplot(x=df["age"])

sns.violinplot(data=df, x="age", inner_kws=dict(box_width=15, whis_width=2, color=".8"))
plt.show()

sns.violinplot(data=df, x="class", y="age", hue="alive", split=True, inner="quart")
plt.show()

sns.violinplot(data=df, x="class", y="age", hue="alive", split=True, gap=.1, inner="quart")
plt.show()
