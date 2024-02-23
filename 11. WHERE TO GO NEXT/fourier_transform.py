import numpy as np
import matplotlib.pyplot as plt

# Generate a simple signal
fs = 1000  # Sampling frequency
t = np.arange(0, 1, 1/fs)  # Time vector
f1 = 5  # Frequency of the signal
f2 = 50  # Frequency of another component
signal = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)  # Composite signal

# Perform FFT
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(signal), 1/fs)

# Plot the signal
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Plot the FFT result
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(fft_result))
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
