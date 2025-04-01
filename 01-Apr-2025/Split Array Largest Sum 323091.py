# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def good(sub_sum):
            curr_sum = 0
            subarrays = 1
            max_sub_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > sub_sum:
                    subarrays += 1
                    curr_sum = num

                max_sub_sum = max(max_sub_sum, curr_sum)
            
            return max_sub_sum, k >= subarrays

        
        left, right = 0, sum(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            max_sum, isCapable = good(mid)

            if isCapable:
                ans = max_sum
                right = mid - 1
            else:
                left = mid + 1
        
        return ans