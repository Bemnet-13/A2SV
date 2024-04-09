from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str):
        window_size = len(p)
        target = Counter(p)
        window = Counter(s[:window_size])
        anagram_idx = []

        for i in range(window_size, len(s) + 1):
            if window == target:
                anagram_idx.append(i-window_size)
            if i == len(s):
                break
            window[s[i]] += 1
            window[s[i-window_size]] -= 1

        return anagram_idx