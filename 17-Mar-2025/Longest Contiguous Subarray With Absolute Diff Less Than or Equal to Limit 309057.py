# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_ = deque()
        max_ = deque()
        left = 0
        max_length = 0

        for i in range(len(nums)):
            # Create a mono-queue - decreasing
            while max_ and max_[-1] > nums[i]:
                max_.pop()

            while min_ and min_[-1] < nums[i]:
                min_.pop()
            
            max_.append(nums[i])
            min_.append(nums[i])

            while left < i and abs(max_[0] - min_[0]) > limit:
                if nums[left] == max_[0]:
                    max_.popleft()
                elif nums[left] == min_[0]:
                    min_.popleft()
                
                left += 1

            max_length = max(max_length, i - left + 1)

        return max_length 