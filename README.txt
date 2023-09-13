CSC 311 Scheduling Algorithms Simulator Project

Authors: Mac Coleman, Brodie McCuen, Torii Gresikalns. Block 1, 2023.

This project provides a simulator for different scheduling algorithms.

USAGE:
The accepted command line arguments are of the following form:
python simulator.py [-v | -h] INPUT_FILE [ALGORITHM [PARAMETERS ...]]

Optional arguments:
    -h, --help     :  display usage information about the program
    -v, --version  :  display version information

If either of the above flags are unset, it is assumed that you want to run the simulator.
INPUT_FILE is a required positional argument. It should be the path to a .csv or .txt trace file.

If an INPUT_FILE is specified, the ALGORITHM argument is required. Depending on the value of ALGORITHM, additional
PARAMETERs might be required. The following table displays the available algorithms, which can be specified using either
the algorithm number or name.

SUPPORTED ALGORITHMS:

number    name    description & parameters
******************************************
   1      fcfs     First-come, first serve. Processes that arrive first are scheduled and executed first.
                     No positional parameters are required.
   2       rr      Round robin. Processes are executed for a maximum amount of time before being switched.
                     [QUANTUM] - The maximum burst time each process can use before being evicted from the processor.
   3     sjf_co    Shortest Job First, without preemption.
                     No positional parameters.
   4     sjf_pr    Shortest Job First, with preemption.
                     No positional parameters.
   5    priority   Processes are executed in order of priority, without preemption.
                     No positional parameters.

EXAMPLES:

python simulator.py -v
 -- prints version information to standard output.
python simulator.py -h
 -- prints usage information to standard output.
python simulator.py trace.txt fcfs
 -- runs the simulator on the process trace in trace.txt, with the first-come-first-serve algorithm.
python simulator.py trace.csv rr 4
 -- runs the simulator on the process trace in trace.csv, with the round robin scheduling algorithm with a maximum burst time of 4 units.
python simulator.py trace.csv 3
 -- runs the simulator on the process trace in trace.csv, with the shortest-job-first scheduling algorithm.

TRACE FILE FORMAT SPECIFICATIONS:

As input .txt and .csv files should contain traces of processes for the simulator to run.
All .csv and .txt files MUST contain these four columns, in exactly this order, from left to right:

  PID: Process ID
  arrival_time: The time at which the process arrives to be scheduled.
  cpu_bursts: The remaining length of the process until it is terminated.
  priority: The priority of the process. This is required, even if you do not intend to use an algorithm that requires priority. It will simply be ignored.

All of the values in each column MUST be non-negative integers.
Processes with lower numbers in the priority column are considered higher priority than those with a high number in the priority column.

The following is an example of a trace written in the .csv/.txt format.
Please note that the columns do not have headers. Please do not include headers in your .csv/.txt trace files.
An error will be produced if you do.

TRACE EXAMPLE:

    1,4,10,4
    2,1,20,4
    5,9,32,5
    7,9,19,9
    8,3,15,2

This trace file begins with a process with PID 1 arriving at time 4, with a burst length of 10 and a priority of 4.

OUTPUT FILES:

The program will produce three output files: schedule.txt, wait_times.txt, and statistics.txt.

schedule.txt

  schedule.txt is a comma-separated-value file in which each line represents a process that was executed on the CPU.
  The lines of schedule.txt are arranged in order, so the first process to have been run will be the first process line,
  the second line will be the second process to run, and so on.

  The exact columns of schedule.txt are as follows, from left to right:

    Timestamp: The time at which the process began executing.
    PID: The PID of the process that was executed.
    Burst length: The number of CPU bursts that the process executed before it left the processor.
    Time remaining: The number of CPU bursts that had yet to be completed by the time the process left the processor.

wait_times.txt

  wait_times.txt is a comma-separated-value file in which each line represents a process that was executed on the CPU.
  This file will only contain one line for each process in the trace file, with two columns in each line.

  The columns of wait_times.txt are as follows:

    PID: The process ID of the process that was executed.
    Wait time: The amount of CPU time units that the process spent waiting in the ready queue, not being executed, before it was completed.

statistics.txt

  statistics.txt is a text file containing information about the trace that was just completed.
  This file contains information such as the minimum, maximum, and mean waiting time in a human-readable format.
  It also displays the standard deviation of the waiting times.

ERRORS:

Errors that we have determined are incompatible with continuing the program will immediately cause the program to exit.
However, errors which can be corrected or ignored will allow the program to continue without the erroneous information.
For example, trace files containing invalid lines will simply have their invalid lines ignored,
unless all lines are invalid, in which case the simulator will not run.

SAMPLE TRACES:

Examples of trace files are included with this project.

  trace_test_10.csv, trace_test_100.csv, and trace_test_1000.csv each contain
    10, 100, and 1000 lines of processes to simulate, with differing arrival times, lengths, and priorities.
    They are good examples of well-formed input trace files.

  gaps.csv is a trace file containing two processes, in which there is a long gap between the end of the
    first process and the beginning of the second. It is intended to verify that the simulator can handle
    gaps in between processes.

  same_arrival.csv is a trace file containing several processes that start at the same time.
    It is intended to verify that the simulator can handle processes arriving simultaneously.

  invalid.csv is an example of trace file that is not-well-formed. It will produce error messages,
    but some of its lines can be interpreted and run.
  
  all_invalid.csv is an example of a trace file that is extremely poorly-formed. Not a single line
    can be correctly interpreted, and it will produce an error message that the simulator can not
    continue.