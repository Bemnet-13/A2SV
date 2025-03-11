# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n == 0 or n == 1:
                return 1
            return n * fact(n - 1)
        
        def counter(num):
            if num % 10 != 0:
                return 0
            
            return 1 + counter(num // 10)

        return counter(fact(n))