import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Filter specifications
passband_edge = 1500  # Hz
transition_width = 500  # Hz
Fs = 10000  # Sampling frequency
filter_length = 67

# Normalize the frequencies
nyquist = Fs / 2
passband_edge /= nyquist
transition_width /= nyquist

# Design the Lowpass FIR filter using Blackman window
fir_coefficients = firwin(filter_length, passband_edge, window='blackman', pass_zero=True)

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
plt.plot(0.5 * Fs * w / np.pi, np.abs(h), 'b')
plt.axvline(1500, color='r', linestyle='--', label='Passband edge')
plt.title('Frequency Response of the Lowpass FIR Filter')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
