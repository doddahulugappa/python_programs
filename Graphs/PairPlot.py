import matplotlib.pyplot as plt
import seaborn as sns
penguins = sns.load_dataset("penguins")
sns.pairplot(penguins)
plt.show()

sns.pairplot(penguins, hue="species")
plt.show()

sns.pairplot(penguins, hue="species", corner=True)
plt.show()

sns.pairplot(penguins, hue="species", diag_kind="hist")
plt.show()

sns.pairplot(penguins, hue="species", markers=["o", "s", "D"])
plt.show()

