# Problem: Maximum Number of Vowels in a Substring of Given Length - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        counter = Counter(s[:k - 1])
        max_vowels = 0
        for end in range(k - 1, len(s)):
            counter[s[end]] += 1
            max_vowels = max(max_vowels, self.vowelCounter(counter))
            counter[s[end - k + 1]] -= 1
        return max_vowels

    def vowelCounter(self, counter):
        return counter['a'] +  counter['e'] +  counter['i'] +  counter['o'] +  counter['u'] 