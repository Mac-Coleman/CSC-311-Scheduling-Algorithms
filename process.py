@dataclass
class Process:
    pid: int
    arrival_time: int
    burst_time: int
    priority: int | None # We will not always be using a priority algorithm so priority can be an integer or None.