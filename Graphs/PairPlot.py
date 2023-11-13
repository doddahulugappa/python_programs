import matplotlib.pyplot as plt
import sns as sns
import seaborn as sns
penguins = sns.load_dataset("penguins")
sns.pairplot(penguins)
plt.show()

sns.pairplot(penguins, hue="species")
plt.show()


sns.pairplot(penguins, hue="species", diag_kind="hist")
plt.show()

sns.pairplot(penguins, hue="species", markers=["o", "s", "D"])
plt.show()

