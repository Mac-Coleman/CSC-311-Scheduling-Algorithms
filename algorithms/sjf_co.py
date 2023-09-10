"""
Assigned maintainer: Torii
"""

from process import Process, ProcessExecutionRecord

def simulate_sjf_co(arriving_processes: [Process]) -> ([ProcessExecutionRecord], {int : int}):
    processes_sorted=[Process]
    per_list=[ProcessExecutionRecord]
    wait_times={int:int}
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
                    per_list.append(ProcessExecutionRecord(p.pid,clock,p.burst_time))
                    clock+=p.burst_time
                    wait_times.update({p.pid:(clock-p.arrival_time)})
                    processes_sorted.remove(p)
                    
    return {per_list,wait_times}