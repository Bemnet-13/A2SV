from collections import deque
class MyStack:

    def __init__(self):
        self.front = deque()
        self.back = deque()

    def push(self, x: int) -> None:
        self.front.append(x)
        self.back.appendleft(x)

    def pop(self) -> int:
        self.back.popleft()
        self.front.pop()

    def top(self) -> int:
        if self.back:
            return self.back[0]
        
    def empty(self) -> bool:
        if len(self.front) == 0:
            return True
        return False