# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left <= right:
            mid = (left + right) // 2
            curr = mid * mid
            if curr == x:
                return mid
            elif curr > x:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1
