import heapq

class PRIORITY:
    def __init__(self):
        self.queue = []

    def EMPTY(self):
        return len(self.queue) == 0

    def ADD(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def POP(self):
        if self.EMPTY():
            return None
        return heapq.heappop(self.queue)[1]

    def TOP(self):
        if self.EMPTY():
            return None
        return self.queue[0][1]