# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = { 0 : 1}
        subarrays = 0
        sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i] % 2
            
            if sum_ - k in count:
                subarrays += count[sum_ - k]
            
            count[sum_] = count.get(sum_, 0) + 1
        
        return subarrays