# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = end = score = max_score = 0
        seen = set()

        while end < len(nums):
            if nums[end] not in seen:
                seen.add(nums[end])
                score += nums[end]
                end += 1
            else:
                seen.remove(nums[start])
                score -= nums[start]
                start += 1
            max_score = max(max_score, score)
        
        return max_score