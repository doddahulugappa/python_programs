import matplotlib.pyplot as plt

# Sample data
x = [0, 1, 2, 3, 4, 5, 6]
y1 = [0, 1, 4, 9, 16, 25, 36]
y2 = [0, 1, 0, 1, 0, 1, 0]
y3 = [36, 25, 16, 9, 4, 1, 0]

# Create the plot
fig, ax = plt.subplots()

# Plot the lines
ax.plot(x, y1, color='gray', alpha=0.5, label='Line 1')
ax.plot(x, y2, color='gray', alpha=0.5, label='Line 2')
ax.plot(x, y3, color='gray', alpha=0.5, label='Line 3')

# Highlight the second line
ax.plot(x, y2, color='blue', linewidth=2.5, label='Highlighted Line')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multi-Line Chart with Highlighted Line')

# Adding a legend
plt.legend()

# Show the plot
plt.show()
