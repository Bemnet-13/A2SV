# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        k = int(sqrt(c))
        lst = [i for i in range(k + 1)]
        left = 0
        right = len(lst) - 1
        
        while left <= right:
            if lst[left]**2 + lst[right]**2 == c:
                return True
            elif lst[left]**2 + lst[right]**2 < c:
                left += 1
            else:
                right -= 1
        
        return False