# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            corr_pos = nums[i] - 1
            if nums[corr_pos] == nums[i]:
                i += 1
            else:
                nums[i], nums[corr_pos] = nums[corr_pos], nums[i]
        
        ans = []
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                ans.extend([nums[i], i + 1])
        return ans
        