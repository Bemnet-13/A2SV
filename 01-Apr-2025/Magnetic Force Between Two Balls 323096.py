# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()
        def good(max_force):
            gaps = 1
            curr = 0
            for i in range(len(position)):
                if position[i] - position[curr] > max_force:
                    curr = i
                    gaps += 1
            
            return m >= gaps + 1

        
        left, right = 0, position[-1]
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans