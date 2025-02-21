# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        longest = 0

        l = r = 0
        while r < len(nums):
            if nums[r] == 1 or (nums[r] == 0 and counter[nums[r]] < 1):
                counter[nums[r]] += 1
                r += 1
            else:
                counter[nums[l]] -= 1
                l += 1
            
            longest = max(longest, counter[1] + counter[0] - 1)
        
        return longest