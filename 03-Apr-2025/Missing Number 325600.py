# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        i = 0
        while i < len(nums):
            corr_pos = nums[i]
            if corr_pos == len(nums) or i == corr_pos:
                i += 1
            else:
                nums[i], nums[corr_pos] = nums[corr_pos], nums[i]
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
