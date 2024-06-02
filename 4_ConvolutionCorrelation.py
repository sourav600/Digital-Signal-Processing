import numpy as np
import matplotlib.pyplot as plt

# Define the sequences
x = np.array([1, 2, 3, 1])
h = np.array([1, 2, 1, -1])

y_conv = np.convolve(x, h)
y_corr = np.correlate(x, h, mode='full')

# Plot the sequences, convolution, and correlation results
plt.figure(figsize=(12, 10))

# Plot sequence x
plt.subplot(2, 2, 1)
plt.stem(x)
plt.title('Sequence x')
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plot sequence h
plt.subplot(2, 2, 2)
plt.stem(h)
plt.title('Sequence h')
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plot convolution result
plt.subplot(2, 2, 3)
plt.stem(np.arange(len(y_conv)), y_conv)
plt.title('Convolution Result')
plt.xlabel('n')
plt.ylabel('Amplitude')

# Plot correlation result
plt.subplot(2, 2, 4)
plt.stem(np.arange(-len(h)+1, len(x)), y_corr)
plt.title('Correlation Result')
plt.xlabel('Lag')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
