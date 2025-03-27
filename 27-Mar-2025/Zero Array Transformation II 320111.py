# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:  
        def good(k):
            change = [0] * len(nums)
            for i in range(k):
                l, r, val = queries[i]
                change[l] += val
                if r + 1 < len(nums): change[r + 1] -= val
            
            ps = list(accumulate(change))
            for i in range(len(nums)):
                if ps[i] < nums[i]:
                    return False
            
            return True
        
        left, right = -1, len(queries)
        ans = -1
        if max(nums) == 0:
            return 0

        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if good(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans