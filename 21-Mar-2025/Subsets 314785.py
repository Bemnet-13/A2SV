# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:   
        ans = []
        def backtrack(path, index):
            nonlocal ans
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                ans.append(path[:])
                backtrack(path, i + 1)
                path.pop()
        
        backtrack([], 0)
        ans.append([])
        return ans
        