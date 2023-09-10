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
    "usage: {} [-v | -h] INPUT_FILE [ALGORITHM [PARAMETERS ...]]\n" \
    "Simulate various scheduling algorithms to produce schedules and waiting time statistics.\n\n" \
    "OPTIONS:\n" \
    "\t-h, --help\t\tprint this help message.\n" \
    "\t-v, --version\t\tprint version information.\n\n" \
    "INPUT_FILE must be either a .csv or .txt file containing process trace information\n"\
    "or a .xml file with configuration information. When INPUT_FILE is a .csv or .txt trace\n" \
    "file, an algorithm must be specified from the table below. Some algorithms require\n" \
    "additional options which must be passed when required.\n\n" \
    "ALGORITHMS:\n" \
    "\tnumber\tname\tdescription\n" \
    "\t*****************************\n" \
    "\t1\tfcfs\tfirst come first serve\n" \
    "\t2\trr\tround robin\n" \
    "\t\t\t[quantum] the time each process gets before it is evicted from the processor.\n" \
    "\t3\tsjf-co\tshortest job first without preemption\n" \
    "\t4\tsjf-pr\tshortest job first with preemption\n\n" \
    "Examples:\n" \
    "\t{} trace.txt rr 4\tSimulate the processes in trace.txt with round robin with a time quantum of 4.\n" \
    "\t{} config.xml\t\tSimulate according to the information in config.xml\n\n" \
    "See the README for more help.\n" \
    "Source online: <https://github.com/Mac-Coleman/CSC-311-Scheduling-Algorithms>"

def handle_help(arguments: dict[str, str | list[str]]) -> None:
    print(help_string.format(name, version, sys.argv[0], sys.argv[0], sys.argv[0]))

def handle_version(arguments: dict[str, str | list[str]]) -> None:
    print(f"{name} {version}")

def handle_trace(arguments: dict[str, str | list[str]]) -> None:
    
    processes = parse_trace(cast(str, arguments["file"]), True)
    (schedule, waiting_times) = simulate_scheduler(processes, cast(str, arguments["algorithm"]), cast(list[str], arguments["parameters"]))
    write_output(schedule, waiting_times)

    print("Arriving processes:")
    for process in processes:
        print(process)

    print("\nSchedule:")
    for record in schedule:
        print(record)
    
    print("\nWaiting times:")
    for (key, value) in waiting_times.items():
        print(f"pid: {key}, time: {value}")

def handle_config(arguments: dict[str, str | list[str]]) -> None:
    pass

if __name__ == "__main__":
    
    arguments = parse_arguments(sys.argv)
    # Decide what to do based on parsed arguments...

    # print(arguments)

    match arguments["action"]:
        case "help":
            handle_help(arguments)
        case "version":
            handle_version(arguments)
        case "use_trace":
            handle_trace(arguments)
        case "ues_config":
            handle_config(arguments)
