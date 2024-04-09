from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        longest = l = r = 0
        while r < len(s):
            c[s[r]] += 1
            if c[s[r]] == 1:
                r += 1
                if sum(c.values()) > longest:
                    longest += 1
            else:
                c[s[l]] -= 1
                del c[s[l]]
                l += 1
        return longest