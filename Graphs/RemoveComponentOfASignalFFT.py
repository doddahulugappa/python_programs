import numpy as np
import matplotlib.pyplot as plt

# Make some data
t = np.linspace(0, 1, 256, endpoint=False)
x = np.sin(2 * np.pi * 3 * t) + np.cos(2 * np.pi * 100 * t)

# Run FFT
X = np.fft.fft(x)

# Zero some channels
X[64:192] = 0

# Run inverse FFT
y = np.fft.ifft(X)

# Plot it
plt.plot(x)
plt.plot(y)
plt.legend(['raw signal', 'filtered signal'])
plt.show()
