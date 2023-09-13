from process import Process, ProcessExecutionRecord
import math
import sys

def simulate_sjf_pr(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:

    if len(args) != 0:
        print(f"Invalid arguments: {args}")
        print("Shortest job first with preemption requires exactly zero parameters.")
        print("")
        print("PARAMETERS:")
        print("\tNone.")
        sys.exit(1)

    schedule: list[ProcessExecutionRecord] = []
    waiting_times: dict[int, int] = {}
    ready_queue: list[Process] = []

    cpu_time = arriving_processes[0].arrival_time
    ready_queue.append(arriving_processes[0])
    next_process = 1

    for process in arriving_processes:
        waiting_times[process.pid] = 0

    while next_process < len(arriving_processes) or len(ready_queue) > 0:

        if len(ready_queue) == 0: # We have not finished all processes but still need to add them to the ready queue!
            # Also, next_process is guaranteed to be valid within this block.

            cpu_time = arriving_processes[next_process].arrival_time # Skip ahead to the next arriving process

            while next_process < len(arriving_processes) and arriving_processes[next_process].arrival_time <= cpu_time:
                ready_queue.append(arriving_processes[next_process])
                next_process += 1


        current_process = choose_shortest(ready_queue) # removes the shortest process from the ready queue.

        max_runtime = current_process.burst_time

        lookahead = next_process
        possible_interruption_time = cpu_time + current_process.burst_time
        if lookahead < len(arriving_processes):
            possible_interruption_time = arriving_processes[next_process].arrival_time

        while lookahead < len(arriving_processes) and arriving_processes[lookahead].arrival_time == possible_interruption_time:
            if arriving_processes[lookahead].burst_time < max_runtime:
                max_runtime = arriving_processes[lookahead].arrival_time - cpu_time
            lookahead += 1

        start_time = cpu_time
        run_time = current_process.execute(max_runtime)
        cpu_time += run_time

        schedule.append(current_process.to_record(start_time, run_time))

        for process in ready_queue:
            waiting_times[process.pid] += run_time
        
        if current_process.burst_time > 0:
            ready_queue.append(current_process)
        
        while next_process < len(arriving_processes) and arriving_processes[next_process].arrival_time <= cpu_time:
            ready_queue.append(arriving_processes[next_process])
            next_process += 1

    return (schedule, waiting_times)

def choose_shortest(processes: list[Process]) -> Process:
    index = 0
    shortest = math.inf
    for i in range(len(processes)):
        if processes[i].burst_time < shortest:
            shortest = processes[i].burst_time
            index = i
    
    return processes.pop(index)
