import numpy as np
import matplotlib.pyplot as plt

# Define the DFT function
def DFT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp(-2j * np.pi * k * n / N)
    return X

# Define the IDFT function
def IDFT(X):
    N = len(X)
    x = np.zeros(N, dtype=complex)
    for n in range(N):
        for k in range(N):
            x[n] += X[k] * np.exp(2j * np.pi * k * n / N)
        x[n] /= N
    return x

# Sample signal: a sum of two sinusoids
Fs = 1000  # Sampling frequency
T = 1/Fs  # Sampling period
t = np.arange(0, 1, T)  # Time vector
f1, f2 = 50, 120  # Frequencies of the sinusoids
x = 0.7 * np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)

# Compute DFT
X = DFT(x)

# Compute IDFT
x_reconstructed = IDFT(X)

# Plot the original and reconstructed signals
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, x)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.stem(np.abs(X))
plt.title('DFT of the Signal')
plt.xlabel('Frequency Bin')
plt.ylabel('Magnitude')

plt.subplot(3, 1, 3)
plt.plot(t, x_reconstructed.real)  # Take the real part as the result should be real
plt.title('Reconstructed Signal from IDFT')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
