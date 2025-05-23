# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            # If the placeholder is 0 and the seeker is non-zeros -> swap
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] != 0:
                left += 1