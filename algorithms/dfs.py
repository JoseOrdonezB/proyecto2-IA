from models.node import Node
from structures.lifo import LIFO

def depth_first_search(graph, initial_state, goal_state):
    root = Node(state=initial_state)

    frontier = LIFO()
    frontier.ADD(root)

    explored = set()

    while not frontier.EMPTY():
        current_node = frontier.POP()

        if current_node.state == goal_state:
            return current_node

        explored.add(current_node.state)

        if current_node.state in graph:
            for neighbor in graph[current_node.state]:

                if neighbor not in explored:
                    child = Node(
                        state = neighbor,
                        parent = current_node,
                        action = f"{current_node.state} -> {neighbor}"
                    )

                    frontier.ADD(child)

    return None