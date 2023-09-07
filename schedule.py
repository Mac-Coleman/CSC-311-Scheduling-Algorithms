from process import Process, ProcessExecutionRecord

class Schedule:
    """
    The schedule class is a dataclass wrapper that is intended to hold a list of process objects in the order in which
    the CPU executed them.
    """
    process_records: [ProcessExecutionRecord]
    current: int = 0

    def __init__(self):
        self.process_records: [ProcessExecutionRecord] = []
        self.current: int = 0

    def peek(self) -> ProcessExecutionRecord:
        if self.current >= len(self.process_records):
            raise IndexError("Attempted to peek next process but there are no processes remaining.")
        return self.process_records[self.current]
    
    def next(self) -> ProcessExecutionRecord:
        if self.current >= len(self.process_records):
            raise IndexError("Attempted to get next process but there are no processes remaining.")
        v = self.process_records[self.current]
        self.current += 1
        return v
    
    def __len__(self) -> int:
        return len(self.process_records)