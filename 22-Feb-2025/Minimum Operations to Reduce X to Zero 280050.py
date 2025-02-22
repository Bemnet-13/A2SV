# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
                
        
        n = len(nums)
        curr_sum = 0
        max_len = -1
        left = 0
        
        for right in range(n):
            curr_sum += nums[right]
            
            while curr_sum >= target and left <= right:
                if curr_sum == target:
                    max_len = max(max_len, right - left + 1)

                curr_sum -= nums[left]
                left += 1

        
        return -1 if max_len == -1 else n - max_len
