# CSC 311 Scheduling Algorithms Simulator Project

### Mac Coleman, Brodie McCuen, Torii Gresikalns. Block 1, 2023.

This project provides a simulator for different scheduling algorithms.

## Usage

The accepted command line arguments are of the following form:
`python simulator.py [-v | -h] INPUT_FILE [ALGORITHM [PARAMETERS ...]]`

Optional arguments:
* `-h`, `--help`: display usage information about the program
* `-v`, `--version`: display version information 

If either of the above flags are unset, it is assumed that you want to run the simulator.
`INPUT_FILE` is a required positional argument. It should be either the path to a .csv or .txt trace file, or the path to a .xml config file.

If `INPUT_FILE` is a .xml file, no further arguments are required, and an error will be produced if more are specified.
If `INPUT_FILE` is a .csv or .txt trace file, the `ALGORITHM` argument is required. Depending on the value of `ALGORITHM`, additional
`PARAMETER`s might be required. The following table displays the available algorithms, which can be specified using either
the algorithm number or name.

### Supported Algorithms

|Number|Name|Description|Required Arguments|
|---|---|---|---|
|1|fcfs|First-come, first-serve. Processes that arrive first are scheduled and executed first.|None|
|2|rr|Round robin.|`QUANTUM`: the maximum burst time each process can use before it is evicted from the processor.|
|3|sjf_co|Shortest Job First, without preemption.|None|
|4|sjf_pr|Shortest Job First, with preemption.|None|

### Examples

* `python simulator.py -v` prints version information to standard output.
* `python simulator.py -h` prints usage information to standard output.
* `python simulator.py trace.txt fcfs` runs the simulator on the process trace in trace.txt, with the first-come-first-serve algorithm.
* `python simulator.py config.xml` runs the simulator based on the settings contained in the config.xml file.
* `python simulator.py trace.csv rr 4` runs the simulator on the process trace in trace.csv, with the round robin scheduling algorithm with a maximum burst time of 4 units.

## Input Formats

### Text / Comma-Separated Value (.txt, .csv)

As inputs, .txt and .csv files should contain traces of processes for the simulator to run. At a minimum, the required columns are:
* PID: Process ID
* arrival_time: The time at which the process arrives to be scheduled.
* cpu_bursts: The remaining length of the process until it is terminated.

All of the above values must be non-negative integers.

The following is an example of a trace written in the .csv format.
```
PID,arrival_time,cpu_bursts
1,4,10
2,1,20
5,9,32
7,9,19
8,3,15
```

### Extensible Markup Language (.xml)

The function of .xml files as input is not yet decided.