# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        
        left = 0
        ans = 0

        for right in range(len(nums)):
            while (left != 0 and (right - left + 1) - (nums[right] - nums[left - 1]) > k) \
            or (right - left + 1) - nums[right] > k:
                left += 1

            ans = max(ans, right - left + 1)

        return ans     