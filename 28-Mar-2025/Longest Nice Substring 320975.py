# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def divide(s):
            if len(s) <= 1:
                return ""
            
            seen = set(s)
            
            for i, letter in enumerate(s):
                opposite_case = letter.swapcase()
                
                if opposite_case not in seen:
                    left = divide(s[:i])
                    right = divide(s[i + 1:])

                    if len(left) >= len(right):
                        return left
                    return right
            
            return s
        
        return divide(s)