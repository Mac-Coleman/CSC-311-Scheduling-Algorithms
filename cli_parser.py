"""
Assigned maintainer: Mac

This script contains the parse_arguments function, which should return a namespace of arguments so
that the calling function will be able to decide what actions to take.
"""


import sys

def parse_arguments(arguments: [str]) -> {str: str}:

    if len(arguments) <= 1 or arguments[1] in ["-h", "--help"]:
        return {"action": "help"}
    
    if arguments[1] in ["-v", "--version"]:
        return {"action": "version"}
    
    if arguments[1].endswith((".txt", ".csv")):
        return {"action": "use_trace"}
    
    elif arguments[1].endswith((".xml")):
        return {"action": "use_config"}
    
    else:
        print("Error: First positional argument must be an input file with a .txt, .csv, or .xml extension.")
        print("Run this program with -h or --help to learn more.")
        sys.exit(1)