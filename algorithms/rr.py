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
    ready_queue: list[Process] = []
    
    cpu_time: int = arriving_processes[0].arrival_time
    ready_queue.append(arriving_processes[0])
    next_process = 1

    for process in arriving_processes:
        waiting_times[process.pid] = 0

    
    while next_process < len(arriving_processes) or len(ready_queue) > 0:

        # Simulate execution of the current process' time quantum
        # Add the processes that arrived during the time quantum to the ready queue
        # Readd the current process to the ready queue if it has any time remaining.

        print(f"next_process:{next_process}, len(arriving_processes): {len(arriving_processes)}")
        print(f"time: {cpu_time}")
        
        current_process = ready_queue.pop(0)

        start_time = cpu_time
        burst_time = current_process.execute(quantum)
        cpu_time += burst_time

        schedule.append(current_process.to_record(start_time, burst_time))
        
        for process in ready_queue:
            waiting_times[process.pid] += 1

        while next_process < len(arriving_processes) and arriving_processes[next_process].arrival_time < cpu_time:
            ready_queue.append(arriving_processes[next_process])
            next_process += 1
        
        if current_process.burst_time > 0:
            ready_queue.append(current_process)
        
        if len(ready_queue) == 0 and next_process < len(arriving_processes):
            cpu_time = arriving_processes[next_process].arrival_time # Skip forward to time of next arriving process.
            while next_process < len(arriving_processes) and arriving_processes[next_process].arrival_time <= cpu_time:
                ready_queue.append(arriving_processes[next_process])
                next_process += 1


    return (schedule, waiting_times)