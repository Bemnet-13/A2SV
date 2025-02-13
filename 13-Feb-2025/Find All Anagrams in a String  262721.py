# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        window = Counter(s[:len(p) - 1])
        ans = []

        for i in range(len(p) - 1, len(s)):
            window[s[i]] += 1
            if window == target:
                ans.append(i - len(p) + 1)
            window[s[i - len(p) + 1]] -= 1
            
        return ans