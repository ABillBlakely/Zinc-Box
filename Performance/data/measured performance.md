# Recorded data from 2017-3-1

## Conditions
88.2 kHz sample rate, 16384 samples, kaiser 7 window, using 100 averages

## Distortion

| Freq (Hz) | Level (dB) | THD (%) | THD+N (%) |
|-----------|------------|---------|-----------|
|       100 |       -3.0 |  0.0099 |     0.055 |
|      1000 |       -3.3 |  0.0034 |     0.067 |
|     10000 |       -2.9 |   0.025 |     0.073 |


| Freqs  (kHz) | Level (dB) | Magnitude ratio | IMD (%) | standard |
|--------------|------------|-----------------|---------|----------|
| 19/20        |       -3.0 | 1:1             |   0.062 | ITU-R    |


## Noise

SNR = -67.0 dB re 0 dB, 44 kHz BW.

The noise figure is dominated by the power line noise, with a peak at 60 Hz of -68.54 dB.
No additional filter was used to limit bandwidth, but the low signal level causes the noise above 20 kHz to be negligible, so the value does not significantly improve by limiting bandwidth.
