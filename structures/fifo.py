class FIFO:
    def __init__(self):
        self.queue = []

    def EMPTY(self):
        return len(self.queue) == 0

    def TOP(self):
        if self.EMPTY():
            return None
        return self.queue[0]

    def POP(self):
        if self.EMPTY():
            return None
        return self.queue.pop(0)

    def ADD(self, item):
        self.queue.append(item)
        return self.queue