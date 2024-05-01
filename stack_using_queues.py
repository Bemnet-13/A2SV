from collections import deque
class MyStack:

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def push(self, x: int) -> None:
        self.front.append(x)

    def pop(self) -> int:
        while len(self.front) > 1:
            val = self.front.popleft()
            self.back.append(val)
        popped_item = self.front[-1]

        self.front, self.back = self.back, self.front
        self.back = deque()
        return popped_item

    def top(self) -> int:
        while len(self.front) >= 0:
            val = self.front.popleft()
            self.back.append(val)
            if len(self.front) == 0:
                last_item = val


        self.front, self.back = self.back, self.front
        self.back = deque()
        return last_item
    
    def empty(self) -> bool:
        if len(self.front) == 0:
            return True
        return False