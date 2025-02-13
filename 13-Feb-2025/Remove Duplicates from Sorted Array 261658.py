# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            # Check if the adjacent numbers are the same
            if nums[right] != nums[left]:
                nums[left] = nums[right]
            
            if nums[left] != nums[left - 1]:
                left += 1
        
        return left
