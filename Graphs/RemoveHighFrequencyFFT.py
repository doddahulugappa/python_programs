import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import rfft, irfft, fftfreq, fft

# Number of sample-points
N = 500
# sample spacing
T = 0.1

x = np.linspace(0.0, (N - 1) * T, N)
# x = np.arange(0.0, N*T, T)  # alternate way to define x
y = 5 * np.sin(x) + np.cos(2 * np.pi * x)

yf = fft(y)
xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
# fft end

f_signal = rfft(y)
W = fftfreq(y.size, d=x[1] - x[0])

cut_f_signal = f_signal.copy()
cut_f_signal[(W > 0.6)] = 0  # filter all frequencies above 0.6

cut_signal = irfft(cut_f_signal)

# plot results
f, axs = plt.subplots(1, 3, figsize=(9, 3))
axs[0].plot(x, y)
axs[0].plot(x, 5 * np.sin(x), 'g')

axs[1].plot(xf, 2.0 / N * np.abs(yf[:N // 2]))
axs[1].legend('numpy fft * dt', loc='upper right')
axs[1].set_xlabel("f")
axs[1].set_ylabel("amplitude")

axs[2].plot(x, cut_signal)
axs[2].plot(x, 5 * np.sin(x), 'g')

plt.show()
