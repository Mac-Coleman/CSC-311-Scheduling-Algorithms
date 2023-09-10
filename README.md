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

As inputs, .txt and .csv files should contain traces of processes for the simulator to run.
All .csv and .txt files *must* contain these four columns, in exactly this order, from left to right:

* PID: Process ID
* arrival_time: The time at which the process arrives to be scheduled.
* cpu_bursts: The remaining length of the process until it is terminated.
* priority: The priority of the process. This is *required*, even if you do not intend to use an algorithm that requires priority. It will simply be ignored.

All of the values in each column *must* be non-negative integers.
Processes with lower numbers in the priority column are considered higher priority than those with a high number in the priority column.

The following is an example of a trace written in the .csv/.txt format.
Please note that the columns *do not* have headers. Please do not include headers in your .csv/.txt trace files.
An error will be produced if you do.
```
1,4,10,4
2,1,20,4
5,9,32,5
7,9,19,9
8,3,15,2
```

### Extensible Markup Language (.xml)

The function of .xml files as input is not yet decided.

## Output files

The program will produce two output files, `schedule.txt`, and `wait_times.txt`.

### schedule.txt

`schedule.txt` is a comma-separated-value file in which each line represents a process that was executed on the CPU.
The lines of `schedule.txt` are arranged in order, so the first process to have been run will be the first process line, the second line will be the second process to run, and so on.

The exact columns of `schedule.txt` are as follows:

* PID: The process ID of the process that was executed.
* Start time: The time at which the process began executing.
* Burst length: The number of CPU bursts that the process executed before it left the processor.
* Time remaining: The number of CPU bursts that had yet to be completed by the time the process left the processor.

### wait_times.txt

`wait_times.txt` is a comma-separated-value file in which each line represents a process that was executed on the CPU.
This file will only contain one line for each process in the trace file, with two columns in each line.

The columns of `wait_times.txt` are as follows:

* PID: The process ID of the process that was executed.
* Wait time: The amount of CPU time units that the process spent waiting in the ready queue, not being executed, before it was completed.