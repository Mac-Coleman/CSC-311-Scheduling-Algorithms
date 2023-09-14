"""
Assigned maintainer: Brodie
"""

from process import ProcessExecutionRecord

def write_output(records: list[ProcessExecutionRecord], waiting_times: dict[int, int], filename: str, algorithm: str) -> str:
    # creates the schedule file
    # writes the execution record information
    schedule_file = open("schedule.txt", 'w')
    for record in records:
        schedule_file.write(f"{record.execution_start_time},{record.pid},{record.burst_time},{record.time_remaining}\n")
    schedule_file.close()

    # creates the waiting times file
    # writes the waiting times dictionary to it
    wait_times_file = open("wait_times.txt", 'w')
    for pid in waiting_times:
        wait_times_file.write(f"{pid},{waiting_times[pid]}\n")
    wait_times_file.close()

    fullname_dict: dict[str, str] = {
        "fcfs": "first come first serve",
        "rr": "round robin",
        "sjf_co": "shortest-job-first",
        "sjf_pr": "shortest-job-first with preemption",
        "priority": "priority",
        "priority_pr": "priority with preemption",
        "1": "first come first serve",
        "2": "round robin",
        "3": "shortest-job-first",
        "4": "shortest-job-first with preemption",
        "5": "priority",
        "6": "priority with preemption"
    }

    algo_name = fullname_dict[algorithm]

    l = f"Statistics for {filename}, with {algo_name} scheduling:\n"

    stats = compute_statistics(list(waiting_times.values()))
    l += f"    Minimum wait time:   {stats[0]:.2f}\n"
    l += f"    Mean wait time:      {stats[2]:.2f}\n"
    l += f"    Maximum wait time:   {stats[1]:.2f}\n"
    l += f"    Standard deviation:  {stats[3]:.2f}\n"
    
    with open("statistics.txt", 'w') as statistics_file:
        statistics_file.write(l)
    
    return l


def compute_statistics(samples: list[int]) -> tuple[int, int, float, float]:
    
    mean: float = 0

    for x in samples:
        mean += x / len(samples)
    
    numerator: float = sum([(x - mean)**2 for x in samples])
    standard_deviation: float = (numerator/len(samples))**0.5

    return min(samples), max(samples), mean, standard_deviation






    