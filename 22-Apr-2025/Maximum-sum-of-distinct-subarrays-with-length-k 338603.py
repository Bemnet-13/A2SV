# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        hashTable = Counter(nums[:k - 1])
        sum_ = sum(nums[:k - 1])
        max_sub_sum = 0

        for i in range(k - 1, len(nums)):
            sum_ += nums[i]
            hashTable[nums[i]] += 1
            if len(hashTable) == k:
                max_sub_sum = max(max_sub_sum, sum_)
            sum_ -= nums[i - k + 1]
            hashTable[nums[i - k + 1]] -= 1
            if hashTable[nums[i - k + 1]] == 0:
                del hashTable[nums[i - k + 1]]
        return max_sub_sum