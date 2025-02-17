# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for i in range(len(nums)):
            left_sum = 0 if i == 0 else nums[i - 1]
            right_sum = 0 if i == len(nums) - 1 else nums[-1] - nums[i]
            if left_sum == right_sum:
                return i
        
        return -1