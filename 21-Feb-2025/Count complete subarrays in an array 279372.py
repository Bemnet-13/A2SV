# Problem: Count complete subarrays in an array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums) -> int:
        distinct= len(set(nums))
        appear = {}
        start = end = count = 0
        while start < len(nums):
            if nums[end] not in appear:
                appear[nums[end]] = 1
            else:
                appear[nums[end]] += 1
            if end < len(nums):
                end += 1
            if len(appear) == distinct:
                end -= 1
                count += len(nums) - end
                appear[nums[end]] -= 1
                if appear[nums[start]] > 0:
                    appear[nums[start]] -= 1
                if appear[nums[end]] == 0:
                    del appear[nums[end]]
                
                if len(appear) == 0:
                    pass
                elif appear[nums[start]] == 0:
                    del appear[nums[start]]
                start += 1
                if start > end:
                    end = start
                
            elif end == len(nums):
                end -= 1
                appear[nums[end]] -= 1
                if appear[nums[start]] > 0:
                    appear[nums[start]] -= 1
                if appear[nums[end]] == 0:
                    del appear[nums[end]]
                if len(appear) == 0 or nums[start] not in appear:
                    pass
                elif appear[nums[start]] == 0:
                    del appear[nums[start]]
                start += 1

        return count
