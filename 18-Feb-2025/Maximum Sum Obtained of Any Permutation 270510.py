# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        changes = [0] * len(nums)

        for left, right in requests:
            changes[left] += 1
            if right + 1 < len(nums): changes[right + 1] -= 1
        
        for i in range(1, len(nums)):
            changes[i] += changes[i - 1]
        
        changes.sort(reverse = True)
        nums.sort(reverse = True)

        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i] * changes[i]
        
        return sum_ % (10**9 + 7)