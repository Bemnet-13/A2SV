# Problem: Sum of Absolute Differences in a Sorted Array - https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ps = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            ps.append(ps[-1] + nums[i])
        
        ans = []

        for i in range(n):
            right_diff = abs((ps[-1] - ps[i]) - (nums[i]) * (n - i - 1))
            left_diff = 0
            if i != 0:
                left_diff = abs(i * nums[i] - (ps[i - 1]))
            
            ans.append(right_diff + left_diff)
        
        return ans

        