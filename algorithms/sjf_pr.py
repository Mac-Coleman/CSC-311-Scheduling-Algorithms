"""
Assigned maintainer: Torii
"""

from process import Process, ProcessExecutionRecord

def simulate_sjf_pr(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:
    clock=0
    current_process_start=0
    current_process_time=0
    current_process=None
    available_processes: list[Process] = []
    wait_times: dict[int,int] = {}
    per_list: list[ProcessExecutionRecord] = []
    while(len(arriving_processes)>0 or len(available_processes)>0):
        dead_list: list[Process]=[]
        for p in arriving_processes:# adding any process that has arrived in this clock cycle to available_processes
            if(wait_times.get(p.pid)==None):
                wait_times[p.pid]=0           
            if(p.burst_time<=clock):
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
                    print("yes")
                current_process=best_process
                current_process_start=clock
                current_process_time=0
                available_processes.remove(best_process)
        else:
            current_process=best_process
            current_process_start=clock
            current_process_time=0
        for p in available_processes:# updates the waits for all processes in the available list
            wait_times[p.pid]=wait_times.get(p.pid)+1
        if(current_process!=None):#only needs to execute for a second because the loop recalculates every clock cycle
            current_process.execute(1)   
            current_process_time+=1
            per_list.append(current_process.to_record(current_process_start,current_process_time))
        clock+=1
    return(per_list,wait_times)