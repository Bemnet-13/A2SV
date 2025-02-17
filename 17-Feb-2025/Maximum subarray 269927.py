# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum_ = 0

        for num in nums:
            sum_ += num
            max_sum = max(max_sum, sum_)
            if sum_ < 0:
                sum_ = 0
        
        return max_sum