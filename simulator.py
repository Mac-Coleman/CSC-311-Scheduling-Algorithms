"""
This file provides the main routine for the scheduling simulator project.
This file must be run in order to start the simulator.
"""

import argparse
import sys

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
    
