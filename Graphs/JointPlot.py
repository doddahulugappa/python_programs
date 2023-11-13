import matplotlib.pyplot as plt
import seaborn as sns
penguins = sns.load_dataset("penguins")


sns.jointplot(penguins, x="bill_length_mm", y="bill_depth_mm", hue="species")
plt.show()

sns.jointplot(penguins, hue="species", x="bill_length_mm", y="bill_depth_mm", kind="hist")
plt.show()

sns.jointplot(penguins, hue="species", x="bill_length_mm", y="bill_depth_mm", markers=["o", "s", "D"])
plt.show()

