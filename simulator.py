"""
This file provides the main routine for the scheduling simulator project.
This file must be run in order to start the simulator.
"""

import sys
from typing import cast

from cli_parser import parse_arguments
from trace_parser import parse_trace
from scheduler import simulate_scheduler
from output_builder import write_output

name = "Schedule Simulator"
version = "0.0.1"

help_string = "{} {}\n" \
    "usage: {} [-v | -h] INPUT_FILE ALGORITHM [PARAMETERS ...]\n" \
    "Simulate various scheduling algorithms to produce schedules and waiting time statistics.\n\n" \
    "OPTIONS:\n" \
    "\t-h, --help\t\tprint this help message.\n" \
    "\t-v, --version\t\tprint version information.\n\n" \
    "INPUT_FILE must be either a .csv or .txt file containing process trace information\n"\
    "An algorithm must be specified from the table below. Some algorithms require\n" \
    "additional options which must be passed when required.\n\n" \
    "ALGORITHMS:\n" \
    "\tnumber\tname\t\tdescription\n" \
    "\t***********************************\n" \
    "\t1\tfcfs\t\tfirst come first serve\n" \
    "\t2\trr\t\tround robin\n" \
    "\t\t\t\t[quantum] the time each process gets before it is evicted from the processor.\n" \
    "\t3\tsjf-co\t\tshortest job first without preemption\n" \
    "\t4\tsjf-pr\t\tshortest job first with preemption\n" \
    "\t5\tpriority\tpriority without preemption\n\n"\
    "Examples:\n" \
    "\tpython {} trace.txt rr 4\tSimulate the processes in trace.txt with round robin with a time quantum of 4.\n" \
    "\tpython {} trace.txt fcfs\tSimulate the processes in trace.txt with first come first serve\n" \
    "\tpython {} trace.txt 3\t\tSimulate the processes in trace.txt with sjf without preemption\n" \
    "\tpython {} -h\t\t\tPrint this usage information.\n\n"\
    "See the README for more help.\n" \
    "Source online: <https://github.com/Mac-Coleman/CSC-311-Scheduling-Algorithms>"

def handle_help(arguments: dict[str, str | list[str]]) -> None:
    print(help_string.format(name, version, sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0], sys.argv[0]))
    # sys.argv[0] here is used to display the file name.

def handle_version(arguments: dict[str, str | list[str]]) -> None:
    print(f"{name} {version}")

def handle_trace(arguments: dict[str, str | list[str]]) -> None:

    filename = cast(str, arguments["file"])
    algorithm = cast(str, arguments["algorithm"])
    parameters = cast(list[str], arguments["parameters"])
    
    processes = parse_trace(filename) # Parse the input file
        
    (schedule, waiting_times) = simulate_scheduler(processes, algorithm, parameters) # Simulate the trace
    stats_string = write_output(schedule, waiting_times, filename, algorithm) # Write the output


    # Display the output in the terminal
    print("\nSchedule:")
    print(f" Timestamp |     PID    |  Burst time remaining")
    for record in schedule:
        print(f"{record.execution_start_time : 10} | {record.pid : 10} | {record.time_remaining: 10}")
        
    
    print("\nWaiting times:")
    print(f"    PID    | Waiting Time")
    for (key, value) in waiting_times.items():
        print(f"{key : 10} | {value : 10}")

    print("\n" + stats_string)

if __name__ == "__main__":
    
    arguments = parse_arguments(sys.argv)
    # Decide what to do based on parsed arguments...

    match arguments["action"]:
        case "help":
            handle_help(arguments)
        case "version":
            handle_version(arguments)
        case "use_trace":
            handle_trace(arguments)
