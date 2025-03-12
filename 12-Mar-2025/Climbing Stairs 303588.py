# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def __init__(self):
        self.cache = {1 : 1, 2 : 2}
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        ans = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = ans
        return ans