class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_count = {}
        for num in nums:
            if num not in color_count:
                color_count[num] = 1
            else:
                color_count[num] += 1
        
        i = 0
        color = 0
        while i < len(nums):
            while color_count.get(color) != None and color_count.get(color) > 0:
                nums[i] = color
                i += 1
                color_count[color] -= 1
            color += 1
