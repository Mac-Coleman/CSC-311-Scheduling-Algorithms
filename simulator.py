"""
This file provides the main routine for the scheduling simulator project.
This file must be run in order to start the simulator.
"""

import sys

from cli_parser import parse_arguments, Action
from trace_parser import parse_trace
from scheduler import simulate_scheduler
from output_builder import write_output

name = "Schedule Simulator"
version = "0.0.1"

if __name__ == "__main__":
    
    argument_action = parse_arguments(sys.argv)
    # Decide what to do based on parsed arguments...

    match argument_action[0]:
        case Action.HELP:
            pass
        case Action.VERSION:
            print(f"{name} {version}")
        case Action.USE_TRACE:
            pass
        case Action.USE_CONFIG:
            pass
