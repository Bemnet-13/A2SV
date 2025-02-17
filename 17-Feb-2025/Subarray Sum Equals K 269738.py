# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = 0
        count = {0 : 1}
        sum_ = 0

        for num in nums:
            sum_ += num
            if sum_ - k in count:
                subarrays += count[sum_ - k]
            
            count[sum_] = count.get(sum_, 0) + 1
        
        return subarrays