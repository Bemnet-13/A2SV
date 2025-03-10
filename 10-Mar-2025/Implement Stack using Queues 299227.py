# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.reserve = deque()
        while len(self.stack) > 1:
            val = self.stack.popleft()
            self.reserve.append(val)
        popped = self.stack.popleft()
        self.stack = self.reserve
        return popped        

    def top(self) -> int:
        self.reserve = deque()
        while self.stack:
            val = self.stack.popleft()
            self.reserve.append(val)
        self.stack = self.reserve
        return val

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()