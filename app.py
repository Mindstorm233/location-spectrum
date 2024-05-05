from flask import Flask, request, render_template
from flask_cors import CORS
import os
import numpy as np
import adi
from scipy.io import savemat
from datetime import datetime

def receive_and_plot_power_spectrum(start_freq, end_freq, lat, lon):
    sample_rate = end_freq - start_freq  # Hz
    if sample_rate >= 61.44e6:
        raise ValueError('Sample Rate must be less than 61.44MHz!')
    if sample_rate <= 0:
        raise ValueError('Sample Rate must not be a negative number!')
    center_freq = (start_freq + end_freq) / 2  # Center frequency
    num_samps = 100000  # number of samples per call to rx()

    sdr = adi.Pluto("ip:192.168.2.1")
    sdr.sample_rate = int(sample_rate)

    # Config Rx
    sdr.rx_lo = int(center_freq)
    sdr.rx_rf_bandwidth = int(sample_rate)
    sdr.rx_buffer_size = num_samps
    sdr.gain_control_mode_chan0 = 'manual'
    sdr.rx_hardwaregain_chan0 = 0.0  # dB, increase to increase the receive gain, but be careful not to saturate the ADC

    # Clear buffer just to be safe
    for i in range(0, 10):
        raw_data = sdr.rx()

    # Receive samples
    rx_samples = sdr.rx()

    # Calculate power spectral density (frequency domain version of signal)
    psd = np.abs(np.fft.fftshift(np.fft.fft(rx_samples))) ** 2
    psd_dB = 10 * np.log10(psd)
    f = np.linspace(start_freq, end_freq, len(psd))

    # Save data to .mat file
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = 'data/' + timestamp + ".mat"
    savemat(filename, {'time':timestamp, 'latitude':lat, 'lontitude':lon, 'f': f, 'psd': psd, 'psd_dB': psd_dB})

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/')
def index():
    return render_template('location.html')

@app.route('/location', methods=['POST'])
def receive_location():
    data = request.json
    print(data)
    print('Received latitude:', data['latitude'])
    print('Received longitude:', data['longitude'])
    start_frequency = float(data['start'])
    end_frequency = float(data['end'])
    try:
        for i in range(1, 31):
            receive_and_plot_power_spectrum(start_frequency, end_frequency, data['latitude'], data['longitude'])
    except ValueError as e:
        return 'Input invalid. ' + str(e)
    print('Data saved.')
    return 'Command received and recorded.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
