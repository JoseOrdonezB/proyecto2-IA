from models.node import Node
from structures.priority import PRIORITY


def a_star_search(graph, heuristics, initial_state, goal_state):

    root = Node(
        state=initial_state,
        cost=0,
        heuristic=heuristics[initial_state]
    )

    frontier = PRIORITY()
    frontier.ADD(root, root.cost + root.heuristic)

    explored = set()

    while not frontier.EMPTY():
        current_node = frontier.POP()

        if current_node.state == goal_state:
            return current_node

        explored.add(current_node.state)

        if current_node.state in graph:
            for neighbor in graph[current_node.state]:

                new_cost = current_node.cost + graph[current_node.state][neighbor]

                if neighbor not in explored:
                    child = Node(
                        state=neighbor,
                        parent=current_node,
                        action=f"{current_node.state} -> {neighbor}",
                        cost=new_cost,
                        heuristic=heuristics[neighbor]
                    )

                    f_value = child.cost + child.heuristic
                    frontier.ADD(child, f_value)

    return None