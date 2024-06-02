import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Filter specifications
passband_edge = 2000  # Hz
stopband_edge = 5000  # Hz
Fs = 20000  # Sampling frequency in Hz
filter_length = 21

# Normalize the frequencies with respect to Nyquist frequency
nyquist = Fs / 2
normalized_passband_edge = passband_edge / nyquist
normalized_stopband_edge = stopband_edge / nyquist

# Design the FIR filter using Hanning window
fir_coefficients = firwin(filter_length, [normalized_passband_edge, normalized_stopband_edge], pass_zero=False, window='hann')

# Frequency response of the filter
w, h = freqz(fir_coefficients, worN=8000, fs=Fs)

# Plot the FIR filter coefficients
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.stem(fir_coefficients)
plt.title('FIR Filter Coefficients')
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plot the frequency response
plt.subplot(2, 1, 2)
plt.plot(w, 20 * np.log10(np.abs(h)), 'b')
plt.axvline(2000, color='g', linestyle='--', label='Passband edge')
plt.axvline(5000, color='r', linestyle='--', label='Stopband edge')
plt.title('Frequency Response of the FIR Filter')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain [dB]')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
