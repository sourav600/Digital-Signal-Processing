import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import tf2zpk

b = [1, -1.5, 0.7]  # Numerator coefficients
a = [1, -0.9, 0.3]  # Denominator coefficients

# Compute zeros, poles, and gain
zeros, poles, gain = tf2zpk(b, a)

# Plot zeros and poles
plt.figure(figsize=(8, 8))
plt.plot(np.real(zeros), np.imag(zeros), 'go', label='Zeros')
plt.plot(np.real(poles), np.imag(poles), 'rx', label='Poles')
plt.title('Pole-Zero Plot')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid()
plt.axhline(0, color='k', linewidth=1)
plt.axvline(0, color='k', linewidth=1)
plt.legend()
plt.show()

# Print zeros, poles, and gain
print("Zeros:", zeros)
print("Poles:", poles)
print("Gain:", gain)
