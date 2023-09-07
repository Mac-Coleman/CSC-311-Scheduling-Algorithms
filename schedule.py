from dataclasses import dataclass
from process import Process

@dataclass
class Schedule:
    """
    The schedule class is a dataclass wrapper that is intended to hold a list of process objects in the order in which
    the CPU executed them.
    """
    processes: [Process]
    current: int = 0

    def peek(self) -> Process:
        if self.current >= len(self.processes):
            raise IndexError("Attempted to peek next process but there are no processes remaining.")
        return self.processes[self.current]
    
    def next(self) -> Process:
        if self.current >= len(self.processes):
            raise IndexError("Attempted to get next process but there are no processes remaining.")
        v = self.processes[self.current]
        self.current += 1
        return v
    
    def __len__(self) -> int:
        return len(self.processes)