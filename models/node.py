class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = heuristic

    def f(self):
        return self.cost + self.heuristic

    def path(self):
        node = self
        states = []

        while node is not None:
            states.append(node.state)
            node = node.parent

        return list(reversed(states))

    def solution(self):
        node = self
        actions = []

        while node.parent is not None:
            actions.append(node.action)
            node = node.parent

        return list(reversed(actions))

    def __repr__(self):
        return f"Node({self.state}, g={self.cost}, h={self.heuristic})"