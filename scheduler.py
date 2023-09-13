"""
simulate_scheduler takes a list of processes and the specified algorithm, and returns 
the tuple that the algorithm functions will all return
"""


from process import Process, ProcessExecutionRecord
from algorithms.fcfs import simulate_fcfs
from algorithms.rr import simulate_rr
from algorithms.sjf_co import simulate_sjf_co
from algorithms.sjf_pr import simulate_sjf_pr
from algorithms.priority import simulate_priority

from typing import Callable

def simulate_scheduler(processes: list[Process], algorithm: str, parameters: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:
    algoDict: dict[str, Callable[[list[Process], list[str]], tuple[list[ProcessExecutionRecord], dict[int, int]]]] = { # dictionary with possible algorithm inputs as keys, and pointers to the correct algorithm function as values
        "fcfs":simulate_fcfs,
        "rr":simulate_rr,        
        "sjf_co":simulate_sjf_co,
        "sjf_pr":simulate_sjf_pr,
        "priority":simulate_priority,
        "1":simulate_fcfs,
        "2":simulate_rr,
        "3":simulate_sjf_co,
        "4":simulate_sjf_pr,
        "5":simulate_priority
    }
    if(algoDict.get(algorithm.lower())!=None): # makes sure the requested algorithm exists, otherwise raises error
        return algoDict[algorithm.lower()](processes, parameters) # returns a tuple with the completed schedule and a dictionary of the wait times
    else:
        raise KeyError('Algorithm Not Found')
