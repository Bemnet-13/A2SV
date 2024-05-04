class Solution:
    def maxOperations(self, nums, k: int) -> int:
        l = 0
        r = len(nums) - 1
        max_ops = 0

        nums.sort()
        while l < r:
            if nums[l] + nums[r] == k:
                max_ops += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        return max_ops