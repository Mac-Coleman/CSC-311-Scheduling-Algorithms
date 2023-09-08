"""
Assigned maintainer: Mac
"""

from process import Process, ProcessExecutionRecord
from trace_parser import parse_trace

def simulate_fcfs(arriving_processes: [Process], args: list) -> [ProcessExecutionRecord]:
    
    cpu_time: int = arriving_processes[0].arrival_time
    execution_schedule: [ProcessExecutionRecord] = []
    waiting_times: {int: int} = {}

    for arriving_process in arriving_processes:
        execution_schedule.append(arriving_process.to_record(cpu_time, arriving_process.burst_time))
        waiting_times[arriving_process.pid] = cpu_time - arriving_process.arrival_time
        cpu_time += arriving_process.burst_time
        
    return execution_schedule, waiting_times