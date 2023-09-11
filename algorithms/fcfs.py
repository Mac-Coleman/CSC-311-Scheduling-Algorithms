"""
Assigned maintainer: Mac
"""

from process import Process, ProcessExecutionRecord

def simulate_fcfs(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:
    
    cpu_time: int = arriving_processes[0].arrival_time
    execution_schedule: list[ProcessExecutionRecord] = []
    waiting_times: dict[int, int] = {}

    for arriving_process in arriving_processes:

        # If the next process has not yet arrived, skip to the time it did.
        if cpu_time < arriving_process.arrival_time:
            cpu_time = arriving_process.arrival_time
        
        # Save the record of the waiting time.
        # This algorithm is not preemptive, so we just have to save the difference
        # between the current time and the arrival time.
        waiting_times[arriving_process.pid] = cpu_time - arriving_process.arrival_time

        # Calculate the time the process spends running.
        starting_time = cpu_time
        running_time = arriving_process.execute(arriving_process.burst_time)
        cpu_time += running_time

        # Save the record of the work done.
        record = arriving_process.to_record(starting_time, running_time)
        execution_schedule.append(record)
        
    return execution_schedule, waiting_times