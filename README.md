# RIAA Preamp

### The feature complete RIAA preamp.

## Introduction.

This RIAA preamp was meant to be a simple, high performance preamp for my personal use.
Version 1 was named the feature complete version because it had none of the typical features of most RIAA preamps. The usual features are gain control and input impedance matching. 

In this repository you will find:
- KiCad contains the project files for schematic capture and PCB creation. In this folder you will also find the Gerber files used for PCB production.
- LTspice folder contains the files used for simulation and testing of project designs.
- Main directory has the current schematic, some reports, and this readme.

Version 2, the current development, is meant to improve on the performance of version 1. V2 may roll in some of the features that were omitted from V1 and will include many improvements electrically and mechanically.

## Performance of V1
V1 offered up some pretty decent performance, but has its issues as well. For a more thorough look at performance, check [Performance V1.0.md](Performance V1.0.md).

- Freq Response within +/- 2 dB of ideal across the audio spectrum.
- Channel matching within +/- 0.25 dB.
- THD < 0.05% 
- IMD < 0.08%

## Intended changes for V2.
Changes will come in two categories, electrical and mechanical. You can see more details for many of these things in the [issue tracker](https://github.com/ABillBlakely/riaa-preamp/issues).

### Electrical
- Closer match to ideal transfer curve.
- Switch for high and low gain.
- Better integration of PCB by moving jacks on board. 
- Reduce power supply noise.
- *Input impedance switch* (maybe).

### Mechanical
- New enclosure design, possibly with silkscreen or engraved panel.
- Change voltage regulators to smaller packages, or lay them flat.
- Better quality DC Jack.

