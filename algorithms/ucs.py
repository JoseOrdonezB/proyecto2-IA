from models.node import Node
from structures.priority import PRIORITY


def uniform_cost_search(graph, initial_state, goal_state):

    root = Node(state=initial_state, cost=0)

    frontier = PRIORITY()
    frontier.ADD(root, root.cost)

    explored = {}

    while not frontier.EMPTY():
        current_node = frontier.POP()

        if current_node.state == goal_state:
            return current_node

        if (current_node.state in explored and
                explored[current_node.state] <= current_node.cost):
            continue

        explored[current_node.state] = current_node.cost

        if current_node.state in graph:
            for neighbor in graph[current_node.state]:
                
                step_cost = graph[current_node.state][neighbor]
                total_cost = current_node.cost + step_cost

                child = Node(
                    state=neighbor,
                    parent=current_node,
                    action=f"{current_node.state} -> {neighbor}",
                    cost=total_cost
                )

                frontier.ADD(child, total_cost)

    return None