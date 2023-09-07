from dataclasses import dataclass
from process import Process

@dataclass
class Schedule:
    processes: [Process]
    current: int = 0

    def peek(self):
        if self.current >= len(self.processes):
            raise IndexError("Attempted to peek next process but there are no processes remaining.")
        return self.processes[self.current]
    
    def next(self):
        if self.current >= len(self.processes):
            raise IndexError("Attempted to get next process but there are no processes remaining.")
        v = self.processes[self.current]
        self.current += 1
        return v