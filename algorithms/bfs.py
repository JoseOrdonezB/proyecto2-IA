import time
from models.node import Node
from structures.fifo import FIFO


def breadth_first_search(maze, initial_state, goal_states):
    start_time = time.time()

    root = Node(state=initial_state, cost=0)

    frontier = FIFO()
    frontier.ADD(root)

    explored = set()
    frontier_states = {initial_state}

    nodes_explored = 0
    total_children = 0

    rows = len(maze)
    cols = len(maze[0])

    while not frontier.EMPTY():
        current_node = frontier.POP()
        frontier_states.remove(current_node.state)

        nodes_explored += 1

        if current_node.state in goal_states:
            end_time = time.time()

            path = current_node.path()

            branching_factor = (
                total_children / nodes_explored if nodes_explored > 0 else 0
            )

            return {
                "path": path,
                "cost": len(path) - 1,
                "nodes_explored": nodes_explored,
                "time": end_time - start_time,
                "branching_factor": branching_factor
            }

        explored.add(current_node.state)

        i, j = current_node.state

        neighbors = [
            (i - 1, j),
            (i, j + 1),
            (i + 1, j),
            (i, j - 1)
        ]

        for ni, nj in neighbors:
            if 0 <= ni < rows and 0 <= nj < cols:
                if maze[ni][nj] != '1':
                    neighbor = (ni, nj)

                    if neighbor not in explored and neighbor not in frontier_states:
                        child = Node(
                            state=neighbor,
                            parent=current_node,
                            action=(ni, nj),
                            cost=current_node.cost + 1
                        )

                        frontier.ADD(child)
                        frontier_states.add(neighbor)

                        total_children += 1

    end_time = time.time()

    return {
        "path": None,
        "cost": None,
        "nodes_explored": nodes_explored,
        "time": end_time - start_time,
        "branching_factor": (
            total_children / nodes_explored if nodes_explored > 0 else 0
        )
    }