import numpy as np
import matplotlib.pyplot as plt
import os

#set the working directory
os.chdir('C:/Users/William/Google Drive/Projects/RIAA Pre/Performance/data')

# Three time constants the RIAA pre is based around
T1 = 3180E-6
T2 = 318E-6
T3 = 75E-6

# Scaling factor K
K = 1 

# create the array of frequencies
f = np.linspace(0,47997.07,16384, endpoint=True)

# The transfer function
H = K*(1+T2*2*np.pi*f*1j)/((1+T1*2*np.pi*f*1j)*(1+T3*2*np.pi*f*1j))

# Get the magnitude in dB
mag = 20 * np.log10(np.abs(H))

# Write the data out to a list of comma separated values for use in excel.
file = open('data/freq resp ideal.txt','w')

for i in range(0,16383):
	s = str(f[i]) + ', ' + str(mag[i]) + '\n'
	file.write(s)

file.close()    



