# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        window_size = len(s)
        max_len = ''
        while window_size:
            for i in range(len(s) - window_size + 1):
                sub = s[i:i+ window_size]
                if self.isNice(sub):
                    return sub
            window_size -= 1
        return ""
    def isNice(self, s):
        characters = set(s)
        for char in characters:
            small = chr(ord(char) + 32)
            cap = chr(ord(char) - 32)

            if not (small in characters or cap in characters):
                return False
        return True