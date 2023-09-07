"""
This file provides the main routine for the scheduling simulator project.
This file must be run in order to start the simulator.
"""

import argparse
import sys
import pandas as pd

from process import Process
from schedule import Schedule

# parses the trace file and returns a list of process objects
# can choose to sort by arrival date
def parse_trace(file_name, sort_arrival=False):
    '''
    file_name: exact file name
    sort_arrival: boolean value if you need to sort by arrival time
    '''
    df = pd.read_csv(file_name, header=None)
    if sort_arrival:
        df = df.sort_values(df.columns[1])
    
    processes = []
    for i in df[0].index.values.tolist():
        # goes by the row of the trace file and makes a process object
        processes.append(Process(df[0][i], 
                                         df[1][i],
                                         df[2][i],
                                         df[3][i]))
    return processes

def simulate(file_name: str) -> Schedule:
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="Scheduling Algorithm Simulator", description="A program to simulate various process scheduling algorithms")

    # We want a version parameter just so the user can check the version.
    parser.add_argument("-v", "--version", action="version", version="%(prog)s v0.0.1")

    # The program must take one positional argument, the input .txt or .xml file
    # So here it is added as a single positional argument.
    parser.add_argument("input", action="store", help="either a .txt trace file or a .xml file containing inputs")

    # Depending on the `input` argument, the algorithm argument may or may not be needed.
    # Here nargs is set to "?" so argparse knows that it is okay if this argument is not present.
    parser.add_argument("algorithm", action="store", nargs="?", help="the algorithm to use.")

    argument_namespace = parser.parse_args()
    print(argument_namespace)

    # We need to validate the inputs so that the user understands what the program can accept.
    if not argument_namespace.input.endswith((".txt", ".csv", ".xml")):
        print(f"{argument_namespace.input} is not a valid input file.")
        print("Valid input file types: .txt, .csv, .xml")
        sys.exit(1)
    
    if argument_namespace.input.endswith(".xml") and argument_namespace.algorithm is not None:
        print(f"Invalid argument: {argument_namespace.algorithm}")
        print("Algorithms can not be specified when a .xml file is the input.")
        sys.exit(1)

    if argument_namespace.input.endswith((".txt", ".csv")):
        # Run the simulator on a single input file.
        pass    
