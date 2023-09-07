from dataclasses import dataclass

@dataclass
class ProcessExecutionRecord:
    pid: int
    execution_start_time: int
    burst_time: int
    priority: int | None

@dataclass
class Process:
    pid: int
    arrival_time: int
    burst_time: int
    priority: int | None # We will not always be using a priority algorithm so priority can be an integer or None.

    def to_record(self, execution_start_time: int, execution_burst_time: int) -> ProcessExecutionRecord:
        return ProcessExecutionRecord(self.pid, execution_start_time, execution_burst_time, self.priority)

if __name__ == "__main__":
    p = Process(5, 2, 3, None)
    print(p)
    r = p.to_record(0, 3)
    print(r)