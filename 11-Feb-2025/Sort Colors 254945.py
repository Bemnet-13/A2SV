# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_1 = num_2 = num_3 = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                num_1 += 1
            elif nums[i] == 1:
                num_2 += 1
            elif nums[i] == 2:
                num_3 += 1

        for i in range(len(nums)):
            if i < num_1:
                nums[i] = 0
            elif i < num_1 + num_2:
                nums[i] = 1
            else:
                nums[i] = 2

        