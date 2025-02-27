# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:   
        n = len(nums)
        odd = [0] * n
        even = [0] * n
        for i in range(n):
            if i % 2: odd[i] = nums[i]
            else: even[i] = nums[i]
        
        for i in range(1, n):
            odd[i] += odd[i - 1]
            even[i] += even[i - 1]

        
        ans = 0
        for i in range(n):
            new_odd = even[-1] - even[i]
            new_even = odd[-1] - odd[i] 
            if i - 1 >= 0:
                new_odd += odd[i - 1]
                new_even += even[i - 1]
            
            if new_odd == new_even:
                ans += 1
        
        return ans