# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0

        ans = 0
        for end in range(len(s)):
            # If the index is not found in the seen
            if s[end] in seen and seen[s[end]] >= start:
                start = seen[s[end]] + 1
            
            seen[s[end]] = end
            ans = max(ans, end - start + 1)
        
        return ans

            
