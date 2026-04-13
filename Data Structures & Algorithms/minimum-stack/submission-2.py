class MinStack:
    from collections import deque

    def __init__(self):
        self.queue = deque()
        self.minq = deque()
        
    def push(self, val: int) -> None:
        self.queue.append(val)
        
        if self.minq:
            self.minq.append(min(self.minq[-1], val))
        else:
            self.minq.append(val)

    def pop(self) -> None:
        self.queue.pop()
        self.minq.pop()

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        return self.minq[-1]
        
