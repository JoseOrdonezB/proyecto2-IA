class LIFO:
    def __init__(self):
        self.stack = []

    def EMPTY(self):
        return len(self.stack) == 0

    def TOP(self):
        if self.EMPTY():
            return None
        return self.stack[-1]

    def POP(self):
        if self.EMPTY():
            return None
        return self.stack.pop()
    
    def ADD(self, item):
        self.stack.append(item)
        return self.stack