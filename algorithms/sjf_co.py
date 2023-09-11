"""
Assigned maintainer: Torii
"""

from process import Process, ProcessExecutionRecord

def simulate_sjf_co(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int,int]]:
    processes_sorted: list[Process] = []
    per_list: list[ProcessExecutionRecord] = []
    wait_times: dict[int,int] = {}
    i=0
    for p in arriving_processes:
        if(p.burst_time<i):
            processes_sorted.insert(i,p)
        else:
            processes_sorted.insert(i+1,p)
    clock=0
    while(len(processes_sorted)>0):
        found=False
        for p in processes_sorted:
            if(p.arrival_time<=clock):
                if(found==False):
                    run_time=p.execute(p.burst_time)
                    per_list.append(p.to_record(clock, run_time))
                    clock+=run_time
                    wait_times.update({p.pid:(clock-p.arrival_time)})
                    processes_sorted.remove(p)
                    
    return (per_list,wait_times)