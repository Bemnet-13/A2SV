# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)
    
    def atMost(self, nums, k):
        counter = Counter()
        left = 0
        subarrays = 0

        for right in range(len(nums)):
            counter[nums[right]] += 1

            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            
            subarrays += right - left + 1
        
        return subarrays