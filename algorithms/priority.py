
from process import Process, ProcessExecutionRecord
from trace_parser import parse_trace
from math import inf

def simulate_priority(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:
    process_queue = []
    time = arriving_processes[0].arrival_time        # time starts at one, csv file
    index = 0
    total_wait_times = {}
    wait_times = {}
    cpu_burst = 0
    schedule = []
    
    # Main Loop
    #   process queue not empty?   process still running?    process still in arriving processes?
    while len(process_queue) > 0 or cpu_burst >= 0 or index < len(arriving_processes):
        # admit a new process to queue if it matches the time
        if index < len(arriving_processes) and arriving_processes[index].arrival_time == time:
            # finds all processes with same arrival time
            same_arrival_time = subset(arriving_processes[index:])
            for new_process in same_arrival_time:
                wait_times[new_process.pid] = 0
                process_queue.append(new_process)
                index += 1

        # time remaining of current process
        cpu_burst -= 1

        # first process -> set initial variables
        if index == 0:
            start_time = time
            current_process = choose_new_process(process_queue)
            cpu_burst = current_process.burst_time
            

        # when a process finishes
        if cpu_burst == 0:
            # write down the record of the process
            schedule.append(current_process.to_record(start_time, current_process.execute(current_process.burst_time)))
        if process_queue != [] and cpu_burst <= 0:
            # choose new process
            current_process = choose_new_process(process_queue)
            process_queue.remove(current_process)
            # move wait times to total wait times
            total_wait_times[current_process.pid] = wait_times[current_process.pid]
            wait_times.pop(current_process.pid)
            # reset variables
            cpu_burst = current_process.burst_time
            start_time = time
            
            

        # increment wait times by 1 each cycle
        for process in wait_times:
            wait_times[process] += 1

        time += 1
        

    return schedule, total_wait_times

### Creates a subset of processes with the same arrival times
def subset(arriving_processes: list[Process]):
    time = arriving_processes[0].arrival_time
    process_list = []
    for process in arriving_processes:
        if process.arrival_time == time:
            process_list.append(process)
        else:
            return process_list
    # assurance reasons
    return process_list



### Find the process in the queue with the highest priority
### Process queue automatically sorted by arrival time
def choose_new_process(process_queue):
    highest_prio = inf
    for process in process_queue:
        if process.priority < highest_prio:
            highest_prio = process.priority
            highest = process

    return highest
        


