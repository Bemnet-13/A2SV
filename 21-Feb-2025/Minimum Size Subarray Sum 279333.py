# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = end = curr_sum = 0
        min_length = len(nums) + 1
        seen = set()
        while end < len(nums):
            if end not in seen:
                curr_sum += nums[end]
                seen.add(end)
            
            if curr_sum >= target:
                min_length = min(min_length, end - start + 1)
                curr_sum -= nums[start]
                start += 1
            else:
                end += 1 
        
        return 0 if min_length == len(nums) + 1 else min_length 
