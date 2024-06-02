import numpy as np
import matplotlib.pyplot as plt

N = 500
Fs = 100 
k = np.arange(N) / Fs   # Time vector

sig = 0.25 + 2 * np.sin(2 * np.pi * 5 * k) + np.sin(2 * np.pi * 12.5 * k) + \
    1.5 * np.sin(2 * np.pi * 20 * k) + 0.5 * np.sin(2 * np.pi * 35 * k)

# Compute the Fourier Transform
F = np.fft.fft(sig)
# Frequency vector
freq = np.fft.fftfreq(N, 1/Fs)

# Plot original signal
plt.subplot(2, 1, 1)
plt.plot(k, sig)
plt.grid(True)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

# Plot the magnitude spectrum
plt.subplot(2, 1, 2)
plt.plot(freq[:N//2], np.abs(F[:N//2]) * 2 / N)  # Only positive frequencies
plt.title('Magnitude Spectrum')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude')
plt.grid(True)

plt.tight_layout()
plt.show()
