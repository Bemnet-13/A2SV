from collections import deque
class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while len(self.requests) > 0 and (t - self.requests[0] > 3000):
            self.requests.popleft()
        return len(self.requests)
    
trial = RecentCounter()