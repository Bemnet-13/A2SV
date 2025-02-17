# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [nums[0]]
        for i in range(1, len(nums)):
            prefix_array.append(nums[i] * prefix_array[-1])
        
        suffix_array = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            suffix_array.append(nums[i] * suffix_array[-1])
        suffix_array = suffix_array[::-1]
        
        ans = []
        for i in range(len(nums)):
            if i == 0: ans.append(suffix_array[i + 1])
            elif i == len(nums) - 1: ans.append(prefix_array[i - 1])
            else: ans.append(prefix_array[i - 1] * suffix_array[i + 1])
        
        return ans