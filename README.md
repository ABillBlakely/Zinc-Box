# The Zinc Box

### The feature complete RIAA preamp.
#### A Cal Poly AES club project.

## Introduction.

The Zinc Box is an RIAA phono preamp meant to be a simple, high performance preamp for my personal use. The V1.0 was developed solely by myself and was lacking in some of the performance metrics. A new version is being developed within the CPSLO AES club to improve the features and performance of the Zinc Box.

In this repository you will find:
- KiCad contains the project files for schematic capture and PCB creation. In this folder you will also find the Gerber files used for PCB production.
- LTspice folder contains the files used for simulation and testing of project designs.
- Main directory has the current schematic, some reports, and this readme.

## Performance of V1
V1 offered up some pretty decent performance, but has its issues as well. For a more thorough look at performance, check [Performance V1.0.md](Performance V1.0.md).

- Freq Response within +/- 2 dB of ideal across the audio spectrum.
- Channel matching within +/- 0.25 dB.
- THD < 0.05%
- IMD < 0.08%

## Goals
For the second version, subject to change as project is established:
- Match ideal freq response to +/- 0.1dB.
- Lower power supply noise (60 Hz < -90 dB).
- Greatly improved enclosure design, appearance.
- Adjustable input loading.
- THD < 0.005% @ 1 kHz, -3dB output level.
- THD+N < 0.05% @ 1kHz, -3dB output level.
- IMD < 0.05% ITU-R, 13 + 14 kHz 1:1 ratio.

## Updates

#### Upcoming Meeting 2017-3-10
The next meeting of the Zinc Box preamp project will be Friday, March 10 at 3:00 in the controls lab (20-112).

For this meeting we will be discussing power supply requirements and the basics of power supply design. This meeting will transition out of the workshop style of th first meeting and into having you all doing the hands on deseign work.

#### 2017-2-24 Meeting
The first meeting held established some of the background of audio testing and measurement.

- I highly recommend you get [ARTA](http://artalabs.hr/), the user manual is pretty good at guiding you through the setup and measurement techniques.
- [Audio Specifications](http://www.rane.com/note145.html) from Rane Audio is a great, succinct, resource for some more detail on the measurements we performed. It also may give you ideas for additional measurements we should make.
- We established some of the goals which are updated in the __Goals__ section above.
- (UPDATE: In room 126.) Next meeting will be Thursday, March 2. We will be performing measurements a little more methodically to produce a new performance report.

## References and Resources
- [RIAA Equalization](https://en.wikipedia.org/wiki/RIAA_equalization) from wikipedia for what the RIAA curve is and the history behind the standard.
- [Audio Specifications](http://www.rane.com/note145.html) from Rane Audio for the what and why of audio measurements.
- [ARTA](http://artalabs.hr/) for performing measurements.
- [High-Performance Audio Applications of the LM833](http://www.ti.com/lit/an/snoa586d/snoa586d.pdf) from Texas instruments will be a major reference for design of the filter.
- [Magnetic Phono Pickup Cartridges](http://sound.whsites.net/articles/cartridge-loading.html) from Elliot Sound Products, a discussion on input loading for phono preamps.
