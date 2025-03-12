# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def __init__(self):
        self.cache = {0 : 1}
    
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        return self.exp(x, n)
    
    def exp(self, x, n):
        if n in self.cache:
            return self.cache[n]
        
        half = self.exp(x, n // 2)
        rem = x if n % 2 else 1
        ans = half * half * rem
        self.cache[n // 2] = half
        self.cache[n] = ans
        return ans