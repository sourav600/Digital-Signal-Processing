import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import iirnotch, lfilter, freqz

# Signal creation
Fs = 100  # Sampling rate
t = np.arange(100) / Fs
s = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 15 * t) + np.sin(2 * np.pi * 30 * t)

# IIR notch filter design to suppress 5 Hz and 30 Hz
def design_notch_filter(freq, Q, Fs):
    w0 = freq / (Fs / 2)
    b, a = iirnotch(w0, Q)
    return b, a

# Design notch filters
Q = 30  # Quality factor
b1, a1 = design_notch_filter(5, Q, Fs)
b2, a2 = design_notch_filter(30, Q, Fs)

# Apply the filters
s_filtered = lfilter(b1, a1, s)
s_filtered = lfilter(b2, a2, s_filtered)

# Plot the original and filtered signals
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, s_filtered)
plt.title('Filtered Signal (5 Hz and 30 Hz suppressed)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()
