import matplotlib.pyplot as plt

days = [50, 80, 70, 80, 40, 20, 20, 20, 70, 20, 60, 20, 80, 50, 40, 50, 20, 60, 60, 60]
bins = [0, 10, 20, 40, 50, 60, 70, 80, 90, 100]
plt.hist(days, bins, histtype='stepfilled', rwidth=0.88)
plt.xlabel('Distance in kms')
plt.ylabel('kilometer count')
plt.title('bike details Histogram')
plt.show()
