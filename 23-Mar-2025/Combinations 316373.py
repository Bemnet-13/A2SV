# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(num, curr):
            nonlocal ans
            curr.append(num)
            if len(curr) == k:
                ans.append(curr[:])

            if len(curr) == k + 1:
                ans.append(curr[1:])
                return

            for i in range(num + 1, n + 1):
                backtrack(i, curr)
                curr.pop()
        
        backtrack(1, [])
        return ans