# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0   
        while i < len(nums):
            corr_pos = nums[i] - 1
            if nums[i] == nums[corr_pos] and i != corr_pos:
                return nums[i]
            elif nums[i] != nums[corr_pos]:
                nums[corr_pos], nums[i] = nums[i], nums[corr_pos]
            else:
                i += 1