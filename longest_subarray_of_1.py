from collections import Counter
class Solution:
    def longestSubarray(self, nums) -> int:
        if nums.count(1) == len(nums):
            return len(nums) - 1
        c = Counter()
        l = r = 0
        max_ones = 0

        while r < len(nums):
            c[nums[r]] += 1
            if c[0] < 2:
                max_ones = max(max_ones, c[1])
                r += 1
            else:             
                while c[0] >= 2:
                    c[nums[l]] -= 1
                    l += 1
                c[nums[r]] -= 1
        
        return max_ones