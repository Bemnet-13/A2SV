class MyCircularQueue:
    def __init__(self, k: int):
        self.circularQueue = ['N'] * 2 * k       
        self.end = 0
        self.k = k
    
    def enQueue(self, value: int) -> bool:

        if not self.isFull():
            self.circularQueue[self.end] = value
            self.circularQueue[self.end + self.k] = value
            if self.end < self.k - 1:
                self.end += 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.circularQueue[self.end] = 'N'
            self.circularQueue[self.end + self.k] = 'N'
            self.end -= 1
            return True
        return False

    def Front(self) -> int:
        return self.circularQueue[0]

    def Rear(self) -> int:
        return self.circularQueue[self.end]

    def isEmpty(self) -> bool:
        if self.circularQueue[0] == 'N':
            return True
        return False

    def isFull(self) -> bool:
        if self.circularQueue[-1] == 'N':
            return False
        return True
        
    def __str__(self) -> str:
        return str(self.circularQueue)