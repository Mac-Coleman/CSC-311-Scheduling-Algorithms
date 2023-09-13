"""
Assigned maintainer: Torii
"""

from process import Process, ProcessExecutionRecord
import math

def simulate_sjf_pr(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:
    clock=0
    current_process=None
    last_process=None
    last_process_start=0
    available_processes: list[Process] = []
    wait_times: dict[int,int] = {}
    per_list: list[ProcessExecutionRecord] = []
    while(len(arriving_processes)>0 or len(available_processes)>0):
        dead_list: list[Process]=[]
        for p in arriving_processes:# adding any process that has arrived in this clock cycle to available_processes
            if(wait_times.get(p.pid)==None):
                wait_times[p.pid]=0           
            if(p.arrival_time<clock):
                available_processes.append(p)
                dead_list.append(p)
        for p in dead_list:
            arriving_processes.remove(p)
        best_process=None
        best_time=float('inf')
        for p in available_processes:# check if any available processes have a shorter burst time then the current one
            if(p.burst_time<best_time):
                best_process=p
                best_time=p.burst_time  
        # swap if a shorter job is found or if current process has ended
        if(current_process!=None):
           if(best_time<current_process.burst_time or current_process.burst_time==0):
                #per_list.append(current_process.to_record(current_process_start,current_process_time))
                if(current_process.burst_time>0):# if current_process has time left, it goes back in line. Otherwise it disappears after being recorded to per_list
                    available_processes.append(current_process)
                current_process=best_process
                available_processes.remove(best_process)
        else:
            current_process=best_process
            last_process=current_process
        for p in available_processes:# updates the waits for all processes in the available list
            wait_times[p.pid]=wait_times.get(p.pid)+1
        if(current_process!=None):#only needs to execute for a second because the loop recalculates every clock cycle
            current_process.execute(1)
            if(last_process!=current_process):
                per_list.append(last_process.to_record(last_process_start,clock-last_process_start))
                last_process=current_process
                last_process_start=clock
        clock+=1
    return(per_list,wait_times)

def simulate_sjf_pr_new(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:
    schedule: list[ProcessExecutionRecord] = []
    waiting_times: dict[int, int] = {}
    ready_queue: list[Process] = []

    cpu_time = arriving_processes[0].arrival_time
    ready_queue.append(arriving_processes[0])
    next_process = 1

    for process in arriving_processes:
        waiting_times[process.pid] = 0

    while next_process < len(arriving_processes) or len(ready_queue) > 0:

        current_process = choose_shortest(ready_queue) # removes the shortest process from the ready queue.
        print(next_process)

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
