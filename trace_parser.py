import pandas as pd

from process import Process

# parses the trace file and returns a list of process objects
# can choose to sort by arrival date
def parse_trace(file_name, sort_arrival=False):
    '''
    file_name: exact file name
    sort_arrival: boolean value if you need to sort by arrival time
    '''
    df = pd.read_csv(file_name, header=None)
    if sort_arrival:
        df = df.sort_values(df.columns[1])
    
    processes = []
    for i in df[0].index.values.tolist():
        # goes by the row of the trace file and makes a process object
        processes.append(Process(df[0][i], 
                                         df[1][i],
                                         df[2][i],
                                         df[3][i]))
    return processes
