import math

def manhattan(state, goal_states):
    x1, y1 = state

    return min(
        abs(x1 - x2) + abs(y1 - y2)
        for (x2, y2) in goal_states
    )


def euclidean(state, goal_states):
    x1, y1 = state

    return min(
        math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        for (x2, y2) in goal_states
    )