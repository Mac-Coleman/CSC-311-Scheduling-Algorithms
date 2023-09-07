"""
This file provides the main routine for the scheduling simulator project.
This file must be run in order to start the simulator.
"""

import sys

from cli_parser import parse_arguments
from trace_parser import parse_trace
from scheduler import simulate_scheduler
from output_builder import write_output

name = "Schedule Simulator"
version = "0.0.1"

help_string = "{} {}\n" \
    "usage: {} [-vh] [input.txt algorithm | input.csv algorithm | input.xml]"

if __name__ == "__main__":
    
    arguments = parse_arguments(sys.argv)
    # Decide what to do based on parsed arguments...

    match arguments["action"]:
        case "help":
            print(help_string.format(name, version, sys.argv[0]))
        case "version":
            print(f"{name} {version}")
        case "use_trace":
            pass
        case "ues_config":
            pass
