# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = float('inf')

        def good(l, m, r):
            if nums[m] > nums[r]:
                return False
            return True     


        while left <= right:
            mid = (left + right) // 2
            ans = min(ans, nums[mid])
            if good(left, mid, right):
                right = mid - 1
            else:
                left = mid + 1
        
        return ans