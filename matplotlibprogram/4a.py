import matplotlib.pyplot as plt

# Pie chart
labels = ['Apples','Bananas', 'Cherries', 'Dates']
sizes = [120, 90, 90, 60]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels,
        startangle=0)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.legend(title='Four Fruits:')
plt.show()