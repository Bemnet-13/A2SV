# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.queue = []


    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        res = self.reverse(self.queue)
        val = res.pop()
        self.queue = self.reverse(res)
        return val 

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
    
    def reverse(self, q):
        stack = []
        while q:
            stack.append(q.pop())
        return stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()