import numpy as np
import matplotlib.pyplot as plt

def generate_signal(duration, sampling_rate, frequencies):
    t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)
    signal = np.sum([np.sin(2 * np.pi * f * t) for f in frequencies], axis=0)
    return t, signal

def plot_signal_and_spectrum(signal, sampling_rate):
    n = len(signal)
    plt.figure(figsize=(10, 6))

    # Plot the signal in time domain
    plt.subplot(2, 1, 1)
    plt.plot(np.arange(n) / sampling_rate, signal)
    plt.title('Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    # Calculate Fourier Transform
    freqs = np.fft.fftfreq(n, d=1/sampling_rate)
    spectrum = np.fft.fft(signal)

    # Plot the frequency spectrum
    plt.subplot(2, 1, 2)
    plt.plot(freqs, np.abs(spectrum))
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')

    plt.tight_layout()
    plt.show()

def main():
    try:
        duration = float(input("Enter duration of the signal (seconds): "))
        sampling_rate = float(input("Enter sampling rate (Hz): "))
        num_components = int(input("Enter number of frequency components: "))
        frequencies = []
        for i in range(num_components):
            freq = float(input(f"Enter frequency of component {i+1} (Hz): "))
            frequencies.append(freq)

        t, signal = generate_signal(duration, sampling_rate, frequencies)
        plot_signal_and_spectrum(signal, sampling_rate)
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
