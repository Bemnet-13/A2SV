# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Find the minimum positive number in the array
        max_num = max(nums)
        min_num = max_num
        for i in range(len(nums)):
            if nums[i] > 0:
                min_num = min(min_num, nums[i])
        if min_num != 1:
            return 1

        i = 0
        while i < len(nums):
            corr_pos = nums[i] - min_num
            if 0 <= corr_pos < len(nums) and nums[corr_pos] == nums[i]:
                i += 1
            elif 0 <= corr_pos < len(nums) and nums[corr_pos] != nums[i]:
                nums[corr_pos], nums[i] =  nums[i], nums[corr_pos]
            else:
                i += 1
        
        for i in range(len(nums)):
            if nums[i] != min_num + i:
                return min_num + i
                
        return min_num + len(nums)
        