# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 1

        for i in range(2, n + 1):
            ans *= i
        
        num = 0
        count = 0
        while ans % 10 == 0:
            ans = ans // 10
            count += 1
        
        return count