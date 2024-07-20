class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)
    def atMost(self, nums, k):
        nice_subarrays = window_size = start = end = 0

        while end < len(nums):
            window_size += nums[end] % 2
            while window_size > k:
                window_size -= nums[start] % 2
                start += 1
            nice_subarrays += end - start + 1
            end += 1
        
        return nice_subarrays