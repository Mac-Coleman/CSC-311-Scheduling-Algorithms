# CSC 311 Scheduling Algorithms Simulator Project

### Mac Coleman, Brodie McCuen, Torii Gresikalns. Block 1, 2023.

This project provides a simulator for different scheduling algorithms.

## Usage

To run the program, simply open your terminal and run `python simulator.py <input> <algorithm>`.
The command line arguments are explained below.

* `input`: The file from which input will be read, in .csv, .txt, or .xml format.
* `algorithm`: The algorithm to use in simulating the trace. This argument can not be specified if an xml file is the input.

## Input Formats

### Text / Comma-Separated Value (.txt, .csv)

As inputs, .txt and .csv files should contain traces of processes for the simulator to run. At a minimum, the required columns are:
* PID: Process ID
* arrival_time: The time at which the process arrives to be scheduled.
* cpu_bursts: The remaining length of the process until it is terminated.
All of the above values must be non-negative integers.

### Extensible Markup Language (.xml)

The function of .xml files as input is not yet decided.