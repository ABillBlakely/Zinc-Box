import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import os
from numpy import pi, abs, log10
from pandas import read_csv, read_table

# set the working directory
os.chdir('C:/Users/boxca/external/Google Drive/Projects/zinc-box/Performance/data')

# MEASURED DATA

# Read and extract data from the arta data export.
# First few rows contain measurement conditions.
meas_param = read_csv('freq resp meas left.csv',
                      header=0,
                      nrows=2,
                      names=['param', 'value'])
samplerate = meas_param['value'][1]
fftsize = int(meas_param['value'][0])

# remaining lines contain freq and mag data.
meas_data = read_csv('freq resp meas left.csv',
                     header=3,
                     names=['freq', 'mag'])

# This freq axis will be used for all further data.
freq = meas_data['freq'].values
meas_mag = meas_data['mag'].values

# Response should be +40dB at 1khz. Adjust so all responses match a 1kHz.
# Find index nearest 1kHz
norm_index = np.searchsorted(freq, 1000)
# Determine appropriate gain
normalization = 40 - meas_mag[norm_index]
# Adjust magnitude.
meas_mag_norm = meas_mag + normalization

# IDEAL DATA

# Three time constants the RIAA pre is based around
T1 = 3180E-6
T2 = 318E-6
T3 = 75E-6

# create the array of frequencies
# freq = np.linspace(0, samplerate/2, 16384, endpoint=False)

# The transfer function
ideal_resp = ((1 + T2 * 2 * pi * freq * 1j)
              / ((1 + T1 * 2 * pi * freq * 1j) * (1 + T3 * 2 * pi * freq * 1j))
              )

# Get the magnitude in dB
ideal_mag = 20 * np.log10(np.abs(ideal_resp))

# Normalize ideal response
# Determine appropriate gain
normalization = 40 - ideal_mag[norm_index]
# Adjust magnitude.
ideal_mag += normalization

# LTSPICE

# determine reccomended setting and print
print('Appropriate spice command:\n'
      '.ac lin {} {} {}'.format(fftsize, freq[1], samplerate/2)
      )
# input('Press a button to continue when spice data is loaded.')

sim_data = read_table('freq resp LTspice.txt', encoding='cp1252')
# print(sim_data.head(5))
sim_mag = sim_data['V(out)'].values
for index, point in enumerate(sim_mag):
    real, imag = point.split(sep=',')
    sim_mag[index] = 20* log10(abs(float(real) + 1j*float(imag)))

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

plt.ion()

resp_fig = plt.figure(1)
plt.semilogx(freq, ideal_mag,
             freq, meas_mag,
             freq, sim_mag)
plt.title('Frequency Response w/o Normalization')
plt.legend(['Ideal', 'Measured', 'Simulated'])
plt.ylim(10, 60)
plt_setup()

resp_norm_fig = plt.figure(2)
plt.semilogx(freq, ideal_mag,
             freq, meas_mag_norm,
             freq, sim_mag_norm)
plt.title('Normalized Frequency Response')
plt.legend(['Ideal', 'Measured', 'Simulated'])
plt.ylim(10, 60)
plt_setup()

error_fig = plt.figure(3)
plt.semilogx(freq, meas_mag_norm - ideal_mag,
             freq, meas_mag - sim_mag)
plt.title('Normalized Error with ideal response')
plt.legend(['Ideal', 'Simulation'])
plt.ioff()
plt.ylim(-3, 3)
plt_setup()
