# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
                
            seen.add(s[right])
            ans = max(ans, len(seen))
        
        return ans
            
