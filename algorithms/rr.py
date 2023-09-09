"""
Assigned maintainer: Mac
"""

from process import Process, ProcessExecutionRecord

def simulate_rr(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:
    # args[0]: QUANTUM - the maximum time a process can use before it is evicted from the processor.

    quantum: int = 0

    if len(args) != 1:
        raise TypeError()
    
    quantum = int(args[0]) # Raise typerror if not possible

    schedule: list[ProcessExecutionRecord] = []
    waiting_times: dict[int, int] = {}
    readyqueue: list[Process] = []
    
    cpu_time: int = arriving_processes[0].arrival_time
    next_process = 0

    

    return (schedule, waiting_times)