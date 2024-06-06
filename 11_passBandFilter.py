import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Filter specifications
fp1 = 0.2  # Normalized passband edge frequency 1
fp2 = 0.35  # Normalized passband edge frequency 2
fs1 = 0.1  # Normalized stopband edge frequency 1
fs2 = 0.425  # Normalized stopband edge frequency 2
M = 32  # Filter length

# Design the bandpass FIR filter
fir_coefficients = firwin(M, [fp1, fp2], pass_zero=False)

# Frequency response of the filter
w, h = freqz(fir_coefficients, worN=8000)

# Plot the FIR filter coefficients
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.stem(fir_coefficients)
plt.title('FIR Filter Coefficients')
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plot the frequency response
plt.subplot(2, 1, 2)
plt.plot(w / np.pi, np.abs(h), 'b')
plt.axvline(fp1, color='r', linestyle='--', label='Passband edge 1')
plt.axvline(fp2, color='g', linestyle='--', label='Passband edge 2')
plt.axvline(fs1, color='r', linestyle='--', label='Stopband edge 1')
plt.axvline(fs2, color='g', linestyle='--', label='Stopband edge 2')
plt.title('Frequency Response of the Bandpass FIR Filter')
plt.xlabel('Normalized Frequency [×π rad/sample]')
plt.ylabel('Gain')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
