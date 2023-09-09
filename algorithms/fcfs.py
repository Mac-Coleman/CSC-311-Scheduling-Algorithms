"""
Assigned maintainer: Mac
"""

from process import Process, ProcessExecutionRecord
from trace_parser import parse_trace

def simulate_fcfs(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:
    
    cpu_time: int = arriving_processes[0].arrival_time
    execution_schedule: list[ProcessExecutionRecord] = []
    waiting_times: dict[int, int] = {}

    for arriving_process in arriving_processes:

        if cpu_time < arriving_process.arrival_time:
            cpu_time = arriving_process.arrival_time
        execution_schedule.append(arriving_process.to_record(cpu_time, arriving_process.burst_time))
        waiting_times[arriving_process.pid] = cpu_time - arriving_process.arrival_time
        cpu_time += arriving_process.burst_time
        
    return execution_schedule, waiting_times