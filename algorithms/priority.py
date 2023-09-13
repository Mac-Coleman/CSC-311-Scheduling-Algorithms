
from process import Process, ProcessExecutionRecord
from trace_parser import parse_trace


def simulate_priority(arriving_processes: list[Process], args: list[str]) -> tuple[list[ProcessExecutionRecord], dict[int, int]]:
    process_queue = []
    time = arriving_processes[0].arrival_time        # time starts at one, csv file
    index = 0
    total_wait_times = {}
    wait_times = {}
    burst = 0
    schedule = []
    
    # Main Loop
    while process_queue != [] or time < 100:
        print("HERE")
        print("time", time)
        # admit a new process to queue if it matches the time
        if index < len(arriving_processes) and arriving_processes[index].arrival_time == time:
            print("subset: ", subset(arriving_processes[index:]))
            for new_process in subset(arriving_processes[index:]):
                wait_times[new_process.pid] = 0
                process_queue.append(new_process)

        if burst > 0:
            burst -= 1

        # first process -> set initial variables
        if index == 0:
            start_time = time
            current_process = choose_new_process(process_queue)
            burst = current_process.burst_time
            index += 1
            

        
        # when a process finishes
        if burst == 0:
            # write down the record of the process
            schedule.append(current_process.to_record(start_time, current_process.burst_time))
            if process_queue != []:
                # choose new process
                current_process = choose_new_process(process_queue)
                process_queue.remove(current_process)
                # move wait times to total wait times
                total_wait_times[current_process.pid] = wait_times[current_process.pid]
                wait_times.pop(current_process.pid)
                # reset variables
                burst = current_process.burst_time
                start_time = time
                index += 1
            

        # increment wait times by 1 each cycle
        for process in wait_times:
            wait_times[process] += 1

        time += 1
        

    return schedule, total_wait_times

### Creates a subset
def subset(arriving_processes: list[Process]):
    time = arriving_processes[0]
    index = 1
    process_list = [arriving_processes[0]]
    try:
        while arriving_processes[index].arrival_time == time:
            process_list.append(arriving_processes[index])
            index += 1
        return process_list
    except:
        return process_list


### Find the process in the queue with the highest priority
### Process queue automatically sorted by arrival time
def choose_new_process(process_queue):
    highest_prio = 0
    for process in process_queue:
        if process.priority > highest_prio:
            highest_prio = process.priority
            highest = process

    return highest
        



if __name__ == "__main__":
    process_list = parse_trace("..\\sample_traces\\trace_test_10")
    print(process_list)
    simulate_priority(process_list, [])

