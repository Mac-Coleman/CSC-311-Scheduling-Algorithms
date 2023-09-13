"""
This script contains the parse_arguments function, which should return a namespace of arguments so
that the calling function will be able to decide what actions to take.
"""


import sys

def parse_arguments(arguments: list[str]) -> dict[str, str | list[str]]:
    """
    Returns a dictionary to help the program understand what action was decided.
    """

    if len(arguments) <= 1 or arguments[1] in ["-h", "--help"]:
        return {"action": "help"}
    
    if arguments[1] in ["-v", "--version"]:
        return {"action": "version"}
    
    if not arguments[1].endswith((".csv", ".txt")):
        # Bad file extension
        print("Error: First positional argument must be an input file with a .txt or .csv extension.")
        print("Run this program with -h or --help to learn more.")
        sys.exit(1)

    # Here, the file argument must end with ".csv" or ".txt"
    assert arguments[1].endswith((".csv", ".txt"))

    if len(arguments) <= 2:
        # Forgot algorithm
        print("Error: no algorithm provided.")
        print("When a trace file is given as input, an algorithm and required options must be specified.")
        print("Run this program with -h or --help to learn more.")
        sys.exit(1)
    
    d: dict[str, str | list[str]] = {
        "action" : "use_trace",
        "file" : sys.argv[1],
        "algorithm" : sys.argv[2],
        "parameters" : sys.argv[3:]
    }

    return d
