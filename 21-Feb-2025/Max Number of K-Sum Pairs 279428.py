# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        max_ops = 0

        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum > k:
                r -= 1
            elif curr_sum < k:
                l += 1
            else:
                max_ops += 1
                l += 1
                r -= 1
        return max_ops