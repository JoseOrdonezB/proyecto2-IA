import pandas as pd

def load_costs(path):
    df = pd.read_excel(path)

    graph = {}

    for _, row in df.iterrows():
        origin = row['Origen']
        destination = row['Destino']
        cost = row['Cost']

        if origin not in graph:
            graph[origin] = {}

        graph[origin][destination] = cost

    return graph

def load_heuristics(path):
    df = pd.read_excel(path)

    heuristic = {}

    for _, row in df.iterrows():
        node = row['Activity']
        value = row['Recovery time after burning 300cal (minutes)']

        heuristic[node] = value

    return heuristic
