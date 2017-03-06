import os

import matplotlib.pyplot as plt
from matplotlib import ticker
from numpy import abs, log10, pi, searchsorted
from pandas import read_csv, read_table

# Check correct directory and switch to data.
try:
    os.chdir('./data')
except:
    print('Please run script from performance directory.')
    exit()


# MEASURED DATA

# Read and extract data from the arta data export.
# First few rows contain measurement conditions.
meas_param_left = read_csv('freq resp meas left.csv',
                           header=0,
                           nrows=2,
                           names=['param', 'value'])
samplerate = int(meas_param_left['value'][1])
fftsize = int(meas_param_left['value'][0])

# remaining lines contain freq and mag data.
meas_data_left = read_csv('freq resp meas left.csv',
                          header=3,
                          names=['freq', 'mag'])

# This freq axis will be used for all further data.
freq = meas_data_left['freq'].values
meas_mag_left = meas_data_left['mag'].values

# Repeat for right channel.
# Freq and mag data.
meas_data_right = read_csv('freq resp meas right.csv',
                           header=3,
                           names=['freq', 'mag'])

# This freq axis will be used for all further data.
meas_mag_right = meas_data_right['mag'].values

# Response should be +40dB at 1khz. Adjust so all responses match a 1kHz.
# Find index nearest 1kHz
norm_index = searchsorted(freq, 1000)
# Determine appropriate gain
normalization = 40 - meas_mag_left[norm_index]
# Adjust magnitude.
meas_mag_left_norm = meas_mag_left + normalization

# IDEAL DATA

# Three time constants the RIAA pre is based around
T1 = 3180E-6
T2 = 318E-6
T3 = 75E-6

# The transfer function
ideal_resp = ((1 + T2 * 2 * pi * freq * 1j)
              / ((1 + T1 * 2 * pi * freq * 1j) * (1 + T3 * 2 * pi * freq * 1j))
              )

# Get the magnitude in dB
ideal_mag = 20 * log10(abs(ideal_resp))

# Normalize ideal response
# Determine appropriate gain
normalization = 40 - ideal_mag[norm_index]
# Adjust magnitude.
ideal_mag += normalization

# LTSPICE

# determine reccomended setting and print
print('Appropriate spice command:\n'
      '.ac lin {} {} {}'.format(fftsize, freq[0], samplerate/2)
      )
# input('Press a button to continue when spice data is loaded.')

sim_data = read_table('freq resp LTspice.txt', encoding='cp1252')
# print(sim_data.head(5))
sim_mag = sim_data['V(out)'].values[:-1]
for index, point in enumerate(sim_mag):
    real, imag = point.split(sep=',')
    sim_mag[index] = 20 * log10(abs(float(real) + 1j * float(imag)))

# Normalize
normalization = 40 - sim_mag[norm_index]
sim_mag_norm = sim_mag + normalization

# PLOTS
# print(plt.style.available)
plt.style.use('seaborn-talk')


def plt_setup():
    plt.xlabel('Freq (Hz)')
    plt.ylabel('Mag (dB)')
    plt.xlim(20, 20000)
    plt.xticks([20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000])
    plt.gca().get_xaxis().set_major_formatter(ticker.ScalarFormatter())
    plt.grid(b=True, which='both', axis='both')
    plt.show()

plt.cla()
plt.ion()

resp_fig = plt.figure(1)
plt.semilogx(freq, meas_mag_left)
plt.title('Measured Frequency Response')
plt.ylim(5, 45)
plt_setup()

resp_norm_fig = plt.figure(2)
plt.semilogx(freq, ideal_mag,
             freq, meas_mag_left_norm,
             freq, sim_mag_norm)
plt.title('Normalized Frequency Response')
plt.legend(['Ideal', 'Measured', 'Simulated'])
plt.ylim(10, 60)
plt_setup()

error_fig = plt.figure(3)
plt.semilogx(freq, meas_mag_left_norm - ideal_mag,
             freq, meas_mag_left_norm - sim_mag_norm)
plt.title('Normalized Error with ideal response')
plt.legend(['Ideal', 'Simulation'])
plt.ylim(-3, 3)
plt_setup()

chan_match_fig = plt.figure(4)
plt.semilogx(freq, meas_mag_left - meas_mag_right)
plt.title('Channel matching')
plt.ioff()
plt.ylim(-1, 1)
plt_setup()


resp_fig.savefig('../figures/Frequency response comparison.png')
resp_norm_fig.savefig('../figures/Normalized response comparison.png')
error_fig.savefig('../figures/Normalized response error.png')
chan_match_fig.savefig('../figures/Channel matching.png')
