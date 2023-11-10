import sys
import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt

data = pd.read_csv('request-data.csv')

data.set_index("time", inplace=True)
plt.plot(data.sales)
plt.show()
f, Pxx = signal.periodogram(data.sales)
plt.plot(f, Pxx)
plt.show()


top_3_periods = {}

# get indices for 3 highest Pxx values
top3_freq_indices = np.flip(np.argsort(Pxx), 0)[:3]

# use indices from previous step to
# get 3 frequencies with the highest power
freqs = f[top3_freq_indices]

# use same indices to get powers as well
power = Pxx[top3_freq_indices]

# we are interested in period, and it is calculated as 1/frequency
periods = 1 / np.array(freqs)

# populate dict with calculated values
top_3_periods['period1'] = periods[0]
top_3_periods['freq1'] = freqs[0]
top_3_periods['power1'] = power[0]

top_3_periods['period2'] = periods[1]
top_3_periods['freq2'] = freqs[1]
top_3_periods['power2'] = power[1]

top_3_periods['period3'] = periods[2]
top_3_periods['freq3'] = freqs[2]
top_3_periods['power3'] = power[2]

print(top_3_periods)

