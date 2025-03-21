# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, seen, index):
            nonlocal ans
            
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if i not in seen:                    
                    path.append(nums[i])
                    seen.add(i)
                    backtrack(path, seen, i)
                    path.pop()
                    seen.remove(i)
        
        backtrack([], set(), 0)
        return ans