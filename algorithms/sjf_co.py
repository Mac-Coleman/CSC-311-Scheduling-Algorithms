"""
Shortest Job First algorithm without any preemption
"""

from process import Process, ProcessExecutionRecord
# dataclasses to make keeping track of the process info and writing the outputs easier

def simulate_sjf_co(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int,int]]:
    sorted_processes: list[Process] = []
    per_list: list[ProcessExecutionRecord] = []
    wait_times: dict[int,int] = {}
    for p in arriving_processes:#sorting all processes into sorted_processes by burst time
        i=0
        while(i<len(sorted_processes)):
            if(p.burst_time<sorted_processes[i].burst_time):
                sorted_processes.insert(i,p)
                i=len(sorted_processes)
            i+=1
        if(i==len(sorted_processes)):
            sorted_processes.insert(i,p)

    clock=0    
    while(len(sorted_processes)>0):#finds the first process in sorted_processes that has already arrived
        found=False
        for p in sorted_processes:
            if(p.arrival_time<=clock):
                if(found==False):#executing the entire burst time because there is no preemption
                    run_time=p.execute(p.burst_time)
                    per_list.append(p.to_record(clock, run_time))
                    wait_times.update({p.pid:(clock-p.arrival_time)}) 
                    clock+=run_time
                    sorted_processes.remove(p)
                    found=True
        if(found==False):#if there is a gap, advance the clock without running any processes
            clock+=1        
    return (per_list,wait_times)