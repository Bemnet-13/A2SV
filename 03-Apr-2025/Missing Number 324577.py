# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_ = n * (n + 1) // 2
        arr = sum(nums)
        return sum_ - arr