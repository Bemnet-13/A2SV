# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = {0 : 1}
        count_ = sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ - k in counter:
                count_ += counter[sum_ - k]
            
            counter[sum_] = counter.get(sum_, 0) + 1
        
        return count_