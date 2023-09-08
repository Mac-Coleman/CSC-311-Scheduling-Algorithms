"""
Assigned maintainer: Torii
"""


from process import Process, ProcessExecutionRecord
from algorithms.fcfs import simulate_fcfs
from algorithms.rr import simulate_rr
from algorithms.sjf_co import simulate_sjf_co
from algorithms.sjf_pr import simulate_sjf_pr

def simulate_scheduler(processes: [Process], algorithm: str, parameters: [str]) -> ([ProcessExecutionRecord], {int, int}):
    pass