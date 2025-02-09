# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges, left: int, right: int):
        covered = set()
        for i, j in ranges:
            for k in range(i, j + 1):
                covered.add(k)
        
        for i in range(left, right+1):
            if i not in covered:
                return False
        
        return True