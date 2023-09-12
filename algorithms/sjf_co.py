"""
Assigned maintainer: Torii
"""

from process import Process, ProcessExecutionRecord

def simulate_sjf_co(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int,int]]:
    processes_sorted: list[Process] = []
    per_list: list[ProcessExecutionRecord] = []
    wait_times: dict[int,int] = {}
    for p in arriving_processes:
        i=0
        while(i<len(processes_sorted)):
            if(p.burst_time<processes_sorted[i].burst_time):
                processes_sorted.insert(i,p)
                i=len(processes_sorted)
            i+=1
        if(i==len(processes_sorted)):
            processes_sorted.insert(i,p)

    clock=0    
    print(processes_sorted)


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
                    found=True
            if(found==False):
               clock+=1
    return (per_list,wait_times)