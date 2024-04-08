class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] == 0:
                l += 1
            if nums[r] == 2:
                r -= 1
            
