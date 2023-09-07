"""
This file provides the main routine for the scheduling simulator project.
This file must be run in order to start the simulator.
"""

import sys

from cli_parser import parse_arguments
from trace_parser import parse_trace
from scheduler import simulate_scheduler
from output_builder import write_output

if __name__ == "__main__":
    
    argument_namespace = parse_arguments(sys.argv)
    # Decide what to do based on parsed arguments...
    pass
