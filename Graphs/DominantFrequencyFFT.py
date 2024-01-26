# import required modules
import numpy as np
from matplotlib import pyplot as plt
from scipy import fftpack

# assign data
x = np.array([1, 2, 1, 0, 1, 2, 1, 0])

# compute DFT with optimized FFT
w = np.fft.fft(x)

# compute frequency associated
# with coefficients
freqs = np.fft.fftfreq(len(x))

# extract frequencies associated with FFT values
for coef, freq in zip(w, freqs):
	if coef:
		print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,
													f=freq))


# Another program

t = np.linspace(0, 1, 500)
x = np.sin(49 * np.pi * t)

X = fftpack.fft(x)

f, (ax0, ax1) = plt.subplots(2, 1)

ax0.plot(x)
ax0.set_ylim(-1.1, 1.1)

ax1.plot(fftpack.fftfreq(len(t)), np.abs(X))
ax1.set_ylim(0, 190)
plt.show()
