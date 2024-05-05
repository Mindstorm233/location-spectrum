import numpy as np
import adi
import matplotlib.pyplot as plt

def receive_and_plot_realtime(start_freq, end_freq):
    sample_rate = 1e6  # Hz
    center_freq = (start_freq + end_freq) / 2  # Center frequency
    num_samps = 10000  # number of samples per call to rx()

    sdr = adi.Pluto("ip:192.168.2.1")
    sdr.sample_rate = int(sample_rate)

    # Config Rx
    sdr.rx_lo = int(center_freq)
    sdr.rx_rf_bandwidth = int(sample_rate)
    sdr.rx_buffer_size = num_samps
    sdr.gain_control_mode_chan0 = 'manual'
    sdr.rx_hardwaregain_chan0 = 0.0  # dB, increase to increase the receive gain, but be careful not to saturate the ADC

    plt.ion()  # Enable interactive mode for dynamic plotting

    # Infinite loop for real-time updating
    while True:
        # Receive samples
        rx_samples = sdr.rx()

        # Calculate power spectral density (frequency domain version of signal)
        psd = np.abs(np.fft.fftshift(np.fft.fft(rx_samples))) ** 2
        psd_dB = 10 * np.log10(psd)
        f = np.linspace(sample_rate / -2, sample_rate / 2, len(psd))

        # Clear previous plot
        plt.clf()

        # Plot freq domain
        plt.plot(f / 1e6, psd_dB)
        plt.xlabel("Frequency [MHz]")
        plt.ylabel("PSD")

        # Update the plot
        plt.pause(0.01)

# Example usage
start_frequency = 900e6
end_frequency = 920e6
receive_and_plot_realtime(start_frequency, end_frequency)
