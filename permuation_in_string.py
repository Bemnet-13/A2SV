from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target = Counter(s1)
        window = Counter(s2[:len(s1)-1])

        i = len(s1) - 1
        while i < len(s2):
            window[s2[i]] += 1
            if target == window:
                return True
            window[s2[i - len(s1) + 1]] -= 1
            i += 1
        
        return False