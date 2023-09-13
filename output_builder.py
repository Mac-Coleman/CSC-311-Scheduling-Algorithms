"""
Assigned maintainer: Brodie
"""

from process import ProcessExecutionRecord

def write_output(records: list[ProcessExecutionRecord], waiting_times: dict[int, int], filename: str, algorithm: str) -> None:
    # creates the schedule file
    # writes the execution record information
    schedule_file = open("schedule.txt", 'w')
    for record in records:
        schedule_file.write(f"{record.pid},{record.execution_start_time},{record.burst_time}\n")
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
        "1": "first come first serve",
        "2": "round robin",
        "3": "shortest-job-first",
        "4": "shortest-job-first with preemption",
        "5": "priority"
    }

    with open("statistics.txt", 'w') as statistics_file:

        statistics_file.write(f"Statistics for {filename}, ran with {algorithm} scheduling:\n\n")

        stats = compute_statistics(list(waiting_times.values()))
        statistics_file.write(f"Minimum wait time:   {stats[0]:.2f}\n")
        statistics_file.write(f"Mean wait time:      {stats[2]:.2f}\n")
        statistics_file.write(f"Maximum wait time:   {stats[1]:.2f}\n")
        statistics_file.write(f"Standard deviation:  {stats[3]:.2f}\n")


def compute_statistics(samples: list[int]) -> tuple[int, int, float, float]:
    
    mean: float = 0

    for x in samples:
        mean += x / len(samples)
    
    numerator: float = sum([(x - mean)**2 for x in samples])
    standard_deviation: float = (numerator/len(samples))**0.5

    return min(samples), max(samples), mean, standard_deviation




def print_output_data(records: list[ProcessExecutionRecord], waiting_times: dict[int, int]) -> None:
    pass

if __name__ == "__main__":
    wait_times = {1:3, 2:55, 3:12, 4:87}

    test_records = []
    for i in range(10):
        test_records.append(ProcessExecutionRecord(i, i*3, i*2, i, None))

    write_output(test_records, wait_times, "test.csv", "idunno")
    