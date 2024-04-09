from collections import Counter
class Solution:
    def longestOnes(self, nums, k: int) -> int:
        c = Counter()
        l = r = max_consecutive = 0

        while r < len(nums):
            c[nums[r]] += 1
            if c[0] <= k:
                max_consecutive = max(max_consecutive, c[0] + c[1])
                r += 1
            else:
                while c[0] > k:
                    c[nums[l]] -= 1
                    l += 1
                c[nums[r]] -= 1
        
        return max_consecutive
