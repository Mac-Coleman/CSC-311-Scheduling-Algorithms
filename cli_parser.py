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
    
    if arguments[1].endswith(".xml"):
        d = {
            "action" : "use_config",
            "file" : sys.argv[1]
            }
        return d
    
    elif not arguments[1].endswith((".csv", ".txt")):
        print("Error: First positional argument must be an input file with a .txt, .csv, or .xml extension.")
        print("Run this program with -h or --help to learn more.")
        sys.exit(1)

    # Here, the file argument must end with ".csv" or ".txt"
    assert arguments[1].endswith((".csv", ".txt"))

    if len(arguments) <= 2:
        print("Error: no algorithm provided.")
        print("When a trace file is given as input, an algorithm and required options must be specified.")
        print("Run this program with -h or --help to learn more.")
        sys.exit(1)
    
    d = {
        "action" : "use_trace",
        "file" : sys.argv[1],
        "algorithm" : sys.argv[2],
        "parameters" : sys.argv[3:]
    }

    return d
