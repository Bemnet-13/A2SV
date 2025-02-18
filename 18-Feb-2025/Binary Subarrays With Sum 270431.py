# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = { 0 : 1}
        sum_ = 0
        subarrays = 0

        for num in nums:
            sum_ += num
            if sum_ - goal in count:
                subarrays += count[sum_ - goal]
            
            count[sum_] = count.get(sum_, 0) + 1
        
        return subarrays