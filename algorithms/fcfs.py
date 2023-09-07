"""
Assigned maintainer: Mac
"""

from process import Process, ProcessExecutionRecord
from trace_parser import parse_trace

def simulate_fcfs(file_name: str) -> [ProcessExecutionRecord]:
    arriving_processes: [Process] = parse_trace(file_name, sort_arrival=True)
    
    cpu_time: int = arriving_processes[0].arrival_time
    execution_schedule: [ProcessExecutionRecord] = []

    for arriving_process in arriving_processes:
        execution_schedule.add_execution_record(arriving_process.to_record(cpu_time, arriving_process.burst_time))
        cpu_time += arriving_process.burst_time
        
    return execution_schedule