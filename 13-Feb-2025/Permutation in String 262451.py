# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        k = len(s1)
        window_ = Counter(s2[:k - 1])

        for i in range(k - 1, len(s2)):
            window_[s2[i]] += 1
            if window_ == target:
                return True
            window_[s2[i - k + 1]] -= 1
        
        return False