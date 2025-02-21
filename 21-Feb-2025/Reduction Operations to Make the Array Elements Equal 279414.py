# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        
        total_operations = 0
        for j in range(1, len(nums)):
            if nums[j] < nums[j - 1]:
                total_operations += j
        
        return total_operations