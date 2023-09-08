"""
Assigned maintainer: Brodie
"""

import random as pd

from process import Process
import math

# parses the trace file and returns a list of process objects
# output is a list of process objects that are sorted by arrival time
def parse_trace(file_name, arrival_time_cutoff=math.inf):
    '''
    file_name: exact file name
    arrival_time_cutoff:
    '''

    trace = open(file_name)
    trace_data = trace.read()

    process_list = []
    process_lines = trace_data.split('\n')
    # each line cooresponds to a process object
    for line in process_lines:
        # variables are specified for readability
        # split at commas due to csv file format
        line = line.split(',')
        process_list.append(Process(pid=int(line[0]), 
                                 arrival_time=int(line[1]),
                                 burst_time=int(line[2]),
                                 priority=int(line[3])))
    trace.close()

    # starts the sorting and organizing of the process list
    sorted_process_list = quick_sort(process_list, 0, len(process_list)-1)
    max_arrival_time = sorted_process_list[-1].arrival_time
    if arrival_time_cutoff >= max_arrival_time:
        # normal return statement
        return sorted_process_list
    
    # if the user specifies a max arrival time
    cutoff_index = max_arrival_time
    for i, process in enumerate(sorted_process_list):
        if process.arrival_time > arrival_time_cutoff:
            cutoff_index = i-1
            break

    # return for shortened process list
    return sorted_process_list[:cutoff_index]



def quick_sort(processes, low, high):
    if low < high:
        pivot = processes[high].arrival_time
        i = low-1
        for j in range(low, high):
            if processes[j].arrival_time <= pivot:
                i = i+1
                processes[i], processes[j] = processes[j], processes[i]
                
        # choose partition then swap the partition spot with the pivot
        partition = i+1
        processes[partition], processes[high] = processes[high], processes[partition]

        # run quick sort again on the lower and upper halves
        quick_sort(processes, low, partition-1)
        quick_sort(processes, partition+1, high)

    return processes

if __name__ == "__main__":
    process_list = parse_trace("sample_traces\\trace_test_100.csv", arrival_time_cutoff=50)
    for process in process_list:
        print("arrival time: ", process.arrival_time)
        print("pid: ", process.pid)

    