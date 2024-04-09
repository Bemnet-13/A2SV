from collections import Counter
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}

        c = Counter()
        i = 0
        while i < k -1:
            if s[i] in vowels:
                c["vowels"] += 1
            else:
                c[s[i]] += 1
            i += 1
        
        max_vowels = 0

        while i < len(s):
            if s[i] in vowels:
                c["vowels"] += 1
            else:
                c[s[i]] += 1
            
            max_vowels = max(max_vowels, c['vowels'])
            
            if s[i - k + 1] in vowels:
                c["vowels"] -= 1
            else:
                c[s[i - k + 1]] -= 1
            
            i += 1
        
        return max_vowels

        