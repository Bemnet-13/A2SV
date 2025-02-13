# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -math.inf
        curr_sum = sum(nums[:k - 1])

        for i in range(k - 1, len(nums)):
            curr_sum += nums[i]
            max_sum = max(curr_sum, max_sum)
            curr_sum -= nums[i - k + 1]
        
        return max_sum / k