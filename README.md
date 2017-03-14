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
- Lower power supply noise (120 Hz < -90 dB).
- Greatly improved enclosure design, appearance.
- Adjustable input loading.
- THD < 0.005% @ 1 kHz, -3dB output level.
- THD+N < 0.05% @ 1kHz, -3dB output level.
- IMD < 0.05% ITU-R, 13 + 14 kHz 1:1 ratio.

## Updates

#### 2017-3-24 Meeting
We discussed power supply design, and probably tried to cover too many topics in not enough depth. The quick recap:

- The objective of a power supply is to provide stable, constant voltage at the right voltage for the circuit. We know our circuit consists of two op amps so we can figure that we need positive and negative supplies, a total voltage of 20 to 30 volts, and current requirements in the 10's of mA.
- Ripple is the AC noise present on what should be a clean DC supply. V1.0 of the project has problems with power supply noise, so reducing this is a priority.
- An AC voltage must be rectified. The two main types are half-wave and full wave rectification. Full wave wave doubles the ripple frequency while reducing the ripple voltage (both good things) at the expense of requiring 4x the parts count of half wave (or a dedicated IC). 
- An RC filter can reduce ripple, but current will cause a voltage drop across the resistor, and at some point capacitors become physically large and/or expensive, and this limits how effective the filter can be.
- Linear regulators are cheap and easy ways to get a specific voltage output. They come in fixed and variable forms, and usually have around 60 dB (thats a reduction by a factor of 1000) of ripple rejection. 

I am asking that you download the LTSpice folder from up above and install [LTSpice](http://www.linear.com/designtools/software/#LTspice). Ive set up a starting point in 'power supply.asc' from which I would like you to adjust C1, C2, and R1 and try to find a combination that keeps ripple less than 30 uV peak to peak. If you have trouble running the sim, make sure that the two MC78XX files are in the same directory as 'power supply.asc'.

When you have some values that work, go on digikey, mouser or similar and see if you can find the parts available at a reasonable cost. Caps will likely need to be Aluminum electrolytic and should be rated for 50V or higher. 

You may wish to modify the circuit for full wave rectification or make other improvements, any and all improvements are welcome, you can also try simulating a negative regulator using the MC7915. I've added some resources down below specific to power supplies. 

The next official meeting will be the first week of the spring quarter, so there is no rush to get this done during finals week. Questions are welcome in the GroupMe, and let me know if you need to be added to that.

#### Upcoming Meeting 2017-3-10
The next meeting of the Zinc Box preamp project will be Friday, March 10 at 3:00 in the controls lab (20-112).

For this meeting we will be discussing power supply requirements and the basics of power supply design. This meeting will transition out of the workshop style of th first meeting and into having you all doing the hands on design work.

#### 2017-2-24 Meeting
The first meeting held established some of the background of audio testing and measurement.

- I highly recommend you get [ARTA](http://artalabs.hr/), the user manual is pretty good at guiding you through the setup and measurement techniques.
- [Audio Specifications](http://www.rane.com/note145.html) from Rane Audio is a great, succinct, resource for some more detail on the measurements we performed. It also may give you ideas for additional measurements we should make.
- We established some of the goals which are updated in the __Goals__ section above.
- (UPDATE: In room 126.) Next meeting will be Thursday, March 2. We will be performing measurements a little more methodically to produce a new performance report.

## References and Resources
- [LM317]() is a common adjustable regulator, this datasheet has lots of example circuits and aplications worth looking at.
- [MC78XX](http://www.onsemi.com/pub/Collateral/MC7800-D.PDF) is a common fixed positive voltage regulator, the MC79XX are the associated negative voltage regulators.
- [Small, Low Current Power Supplies](http://sound.whsites.net/articles/power-supplies2.htm) from Elliot sound products. This is the second time I've linked to this site, there is lots of good info and example projects here.
- [App note 140, Basic Concepts of Linear Regulator and Switching
Mode Power Supplies](http://cds.linear.com/docs/en/application-note/AN140fa.pdf) from Linear Technology covers some info on when to use linear regulator vs a switching regulator.

- [RIAA Equalization](https://en.wikipedia.org/wiki/RIAA_equalization) from wikipedia for what the RIAA curve is and the history behind the standard.
- [Audio Specifications](http://www.rane.com/note145.html) from Rane Audio for the what and why of audio measurements.
- [ARTA](http://artalabs.hr/) for performing measurements.
- [High-Performance Audio Applications of the LM833](http://www.ti.com/lit/an/snoa586d/snoa586d.pdf) from Texas instruments will be a major reference for design of the filter.
- [Magnetic Phono Pickup Cartridges](http://sound.whsites.net/articles/cartridge-loading.html) from Elliot Sound Products, a discussion on input loading for phono preamps.
