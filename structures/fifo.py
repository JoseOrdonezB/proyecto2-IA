from collections import deque

class FIFO:
    def __init__(self):
        self.queue = deque()

    def EMPTY(self):
        return len(self.queue) == 0

    def TOP(self):
        if self.EMPTY():
            return None
        return self.queue[0]

    def POP(self):
        if self.EMPTY():
            return None
        return self.queue.popleft()

    def ADD(self, item):
        self.queue.append(item)
        return self.queue