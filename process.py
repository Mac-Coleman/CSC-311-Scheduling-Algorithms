from dataclasses import dataclass

@dataclass
class ProcessExecutionRecord:
    pid: int
    execution_start_time: int
    burst_time: int
    time_remaining: int
    priority: int | None

@dataclass
class Process:
    pid: int
    arrival_time: int
    burst_time: int
    priority: int | None # We will not always be using a priority algorithm so priority can be an integer or None.

    def to_record(self, execution_start_time: int, execution_burst_time: int) -> ProcessExecutionRecord:
        """
        Creates a new ProcessExecutionRecord based on the information from this process.
        execution_start_time is the time the process began executing in this record.
        execution_burst_time is the duration the process executed for before it terminated or was preempted.
        """
        return ProcessExecutionRecord(self.pid, execution_start_time, execution_burst_time, self.burst_time, self.priority)
    
    def execute(self, time: int) -> int:
        """
        Decrements the remaining burst time of the process by [time] units.
        Used to simulate execution of a process.
        Returns the time for which the process was actually executed.
        """
        before = self.burst_time
        self.burst_time = 0 if time >= self.burst_time else self.burst_time - time
        return before - self.burst_time

if __name__ == "__main__":
    p = Process(5, 2, 3, None)
    print(p)
    r = p.to_record(0, 3)
    print(r)