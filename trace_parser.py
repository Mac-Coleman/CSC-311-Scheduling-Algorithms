from process import Process
import sys

# parses the trace file and returns a list of process objects
# output is a list of process objects that are sorted by arrival time
def parse_trace(file_name: str) -> list[Process]:

    trace_data: str = ""

    try:
        with open(file_name, 'r') as trace:
            trace_data = trace.read()
    except FileNotFoundError as e:
        print(f"Error: File '{file_name}' does not exist!")
        sys.exit(1)

    process_list: list[Process] = []
    process_lines = trace_data.split('\n')

    line_number = 1

    # each line cooresponds to a process object
    for line in process_lines:
        # variables are specified for readability
        # split at commas due to csv file format
        cells = line.split(',')

        try:
            process_list.append(Process(pid=int(cells[0]), 
                                 arrival_time=int(cells[1]),
                                 burst_time=int(cells[2]),
                                 priority=int(cells[3])))
            
            assert len(cells) == 4

        except ValueError as e:
            print(f"Skipping line {line_number}: All values must be integers and be positive or zero.")

            if line_number == 1:
                print("Remember: Trace files should not be given headers.")
                print("See the README for more information.")
        except IndexError as e:
            print(f"Skipping line {line_number}: All lines must have exactly four values.")
        except AssertionError as e:
            print(f"Skipping line {line_number}: All lines must have exactly four values.")

        line_number += 1

    if len(process_list) == 0:
        print("Error: none of the lines of the trace file could be correctly interpreted as processes.")
        print("See the README for information on trace file formatting.")
        print("Exiting.")
        sys.exit(1)

    # starts the sorting and organizing of the process list
    sorted_process_list = quick_sort(process_list, 0, len(process_list)-1)

    return sorted_process_list


### Sorting processes by arrival times
def quick_sort(processes: list[Process], low: int, high: int) -> list[Process]:
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


    