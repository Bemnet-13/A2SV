# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count, n = s.count('1'), len(s)
        return "1" * (count - 1) + '0'* (n - count) + '1'