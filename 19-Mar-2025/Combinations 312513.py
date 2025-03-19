# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(i, curr):
            nonlocal ans 
            curr.append(i)

            if len(curr) == k:
                ans.append(curr[:])
                return
            
            for j in range(i + 1, n + 1):
                backtrack(j, curr)
                curr.pop()

        for i in range(1, n + 1):
            backtrack(i, [])

        return ans