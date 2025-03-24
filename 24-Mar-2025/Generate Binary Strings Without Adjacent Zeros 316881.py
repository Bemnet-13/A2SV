# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def backtrack(path):
            nonlocal ans
            if len(path) == n:
                ans.append("".join(path[:]))
                return
            
            if not path or path[-1] != "0": 
                path.append("0")
                backtrack(path)
                path.pop()
            
            path.append("1")
            backtrack(path)
            path.pop()
        
        backtrack([])
        return ans


            