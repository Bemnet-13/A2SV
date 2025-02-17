# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        store = { 0 : 1}
        subarrays = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum % k in store:
                subarrays += store[curr_sum % k]
            
            store[curr_sum % k] = store.get(curr_sum % k, 0) + 1
        
        return subarrays