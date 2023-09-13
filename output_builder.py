"""
Assigned maintainer: Brodie
"""

from process import ProcessExecutionRecord

def write_output(records: list[ProcessExecutionRecord], waiting_times: dict[int, int]) -> None:
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


    