import numpy as np
import matplotlib.pyplot as plt

Fs = 1000 
t = np.arange(0, 0.5, 1/Fs)
signal = 5 * np.sin(2 * np.pi * 10 * t)

# Sampling
new_Fs = 100 
t_new = np.arange(0, 0.5, 1/new_Fs)
sampled_signal = 5 * np.sin(2 * np.pi * 10 * t_new)

# Quantization
num_bits = 3
quant_levels = 2 ** num_bits
quant_signal = np.round(sampled_signal * quant_levels / max(sampled_signal)) / quant_levels * max(sampled_signal)

# iii) Coding (example with 3-bit PCM)
def PCM_encode(signal, num_bits):
    quant_levels = 2 ** num_bits
    max_val = max(signal)
    min_val = min(signal)
    step_size = (max_val - min_val) / (quant_levels - 1)
    codes = np.round((signal - min_val) / step_size)
    return codes.astype(int)

pcm_codes = PCM_encode(quant_signal, num_bits)

# Print Quantized values and their PCM codes
print("Quantized values and PCM codes:")
for i in range(len(quant_signal)):
    print(f"Sample {i}: Quantized Value = {quant_signal[i]:.2f}, PCM Code = {pcm_codes[i]}")

# Plot the original, sampled, quantized signals and PCM codes
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 2)
plt.stem(t_new, sampled_signal )
plt.title('Sampled Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 3)
plt.stem(t_new, quant_signal)
plt.title('Quantized Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 2, 4)
plt.stem(t_new, pcm_codes)
plt.title('PCM Encoded Signal')
plt.xlabel('Time [s]')
plt.ylabel('Codes')

plt.tight_layout()
plt.show()
