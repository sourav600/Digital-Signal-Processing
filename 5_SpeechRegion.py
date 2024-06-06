import numpy as np
import matplotlib.pyplot as plt

# Generate a synthetic speech signal
Fs = 16000  # Sampling frequency
t = np.linspace(0, 2, 2 * Fs, endpoint=False)

# Silence region
silence = np.zeros(int(0.5 * Fs))

# Voiced region (simulated with a sine wave)
voiced = 0.5 * np.sin(2 * np.pi * 100 * t[:Fs//2])

# Unvoiced region (simulated with white noise)
unvoiced = 0.5 * np.random.randn(Fs//2)

# Combine all regions
speech_signal = np.concatenate((silence, voiced, unvoiced, silence))

# Plot the speech signal with regions marked
plt.figure(figsize=(12, 6))
plt.plot(t, speech_signal)
plt.axvline(x=0.5, color='r', linestyle='--', label='Voiced region start')
plt.axvline(x=1.0, color='g', linestyle='--', label='Unvoiced region start')
plt.axvline(x=1.5, color='b', linestyle='--', label='Silence region start')
plt.title('Speech Signal with Different Regions')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
