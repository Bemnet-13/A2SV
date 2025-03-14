# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        diffs = { 0 : -3, 1: -2, 2 : -1, 3 : 0}
        nums.sort()

        if len(nums) <= 4:
            return 0
        
        min_ = float('inf')
        for i, v in diffs.items():
            min_ = min(nums[len(nums) -1 + v] - nums[i], min_)

        return min_ 