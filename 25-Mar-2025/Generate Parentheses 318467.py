# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(path, count):
            nonlocal ans
            if len(path) == 2 * n:
                ans.append("".join(path))
                return

            for brace in ["(", ")"]:
                if brace == "(" and count["("] < n or \
                brace == ")" and count[")"] < count["("] and count[")"] < n:
                    path.append(brace)
                    count[brace] += 1
                    backtrack(path, count)
                    path.pop()
                    count[brace] -= 1
        
        dct = defaultdict(int)
        backtrack([], dct)
        return ans
