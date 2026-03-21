class PRIORITY:
    def __init__(self):
        self.queue = []

    def EMPTY(self):
        return len(self.queue) == 0

    def TOP(self):
        if self.EMPTY():
            return None
        return self.queue[0][1]

    def POP(self):
        if self.EMPTY():
            return None
        return self.queue.pop(0)[1]

    def ADD(self, item, priority):
        inserted = False
        for i in range(len(self.queue)):
            if priority < self.queue[i][0]:
                self.queue.insert(i, (priority, item))
                inserted = True
                break

        if not inserted:
            self.queue.append((priority, item))

        return self.queue