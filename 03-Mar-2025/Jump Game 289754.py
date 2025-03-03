# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthestIndex = 0
        for i in range(len(nums)):
            if farthestIndex < i: return False
            farthestIndex = max(farthestIndex, i + nums[i])
        return True