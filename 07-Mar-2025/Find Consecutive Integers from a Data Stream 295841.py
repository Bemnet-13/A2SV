# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.size = k
        self.value = value
        self.count = 0

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num == self.value:
            self.count += 1
        while len(self.queue) > self.size:
            val = self.queue.popleft()
            if val == self.value:
                self.count -= 1
        
        return self.count == self.size



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)