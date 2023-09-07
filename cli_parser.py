"""
Assigned maintainer: Mac

This script contains the parse_arguments function, which should return a namespace of arguments so
that the calling function will be able to decide what actions to take.
"""


import sys
from enum import Enum

class Action(Enum):
    VERSION = 0
    HELP = 1
    USE_TRACE = 2
    USE_CONFIG = 3

def parse_arguments(arguments: [str]) -> (Action, {str: str}):

    if len(arguments) <= 1 or arguments[1] in ["-h", "--help"]:
        return (Action.HELP, {})
    
    if arguments[1] in ["-v", "--version"]:
        return (Action.VERSION, {})
    
    if arguments[1].endswith((".txt", ".csv")):
        return (Action.USE_TRACE, {})
    
    elif arguments[1].endswith((".xml")):
        return (Action.USE_CONFIG, {})
    
    else:
        print("Error: First positional argument must be an input file with a .txt, .csv, or .xml extension.")
        print("Run this program with -h or --help to learn more.")
        sys.exit(1)