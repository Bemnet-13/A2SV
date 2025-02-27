# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        reversed = [-num for num in nums]
        return max(self.maxSubArray(nums), self.maxSubArray(reversed))

    def maxSubArray(self, nums):
        max_ = nums[0]
        sum_ = 0
        for num in nums:
            sum_ += num
            if sum_ < 0:
                sum_ = 0
            
            max_ = max(max_, sum_)
        
        return max_