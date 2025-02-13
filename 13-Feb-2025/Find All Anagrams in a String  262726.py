# Problem: Find All Anagrams in a String  - https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        window_size = len(p)
        window = Counter(s[:window_size - 1])
        ans = []

        for i in range(window_size - 1, len(s)):
            window[s[i]] += 1
            if window == target:
                ans.append(i - window_size + 1)
            window[s[i - window_size + 1]] -= 1

        return ans