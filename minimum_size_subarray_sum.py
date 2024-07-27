class Solution:
    def minSubArrayLen(self, target, nums):
        l = r = subarray_sum = 0
        min_length = len(nums) + 1
        while r < len(nums):
            subarray_sum += nums[r]
            if r == len(nums) - 1:
                if subarray_sum < target:
                    break
                else:
                    min_length = min(min_length, r - l + 1)
                    subarray_sum -= (nums[r] + nums[l])
                    l += 1
            elif subarray_sum < target:
                r += 1
            else:
                min_length = min(min_length, r - l + 1)
                subarray_sum -= nums[r] + nums[l]
                l += 1
        
        if min_length > len(nums):
            return 0
        return min_length