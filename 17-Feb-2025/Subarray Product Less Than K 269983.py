# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        curr_prod = 1
        left = 0
        ans = 0

        if min(nums) >= k:
            return 0

        for right in range(len(nums)):
            curr_prod *= nums[right]

            while left < len(nums) and curr_prod >= k:
                curr_prod = curr_prod // nums[left]
                left += 1
                print(curr_prod, left)
            
            ans += right - left + 1
        
        return ans