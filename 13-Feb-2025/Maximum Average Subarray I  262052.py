# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = curr_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            max_sum = max(curr_sum, max_sum)

        return max_sum / k