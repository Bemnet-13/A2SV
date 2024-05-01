class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.headIndex = 0
    def enqueue(self, val):
        self.queue.append(val)
    def dequeue(self):
        if self.headIndex < len(self.queue):
            val = self.queue[self.headIndex]
            self.headIndex += 1
            return val
        return None
