# Problem: Replace the Substring for Balanced String - https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution:
    def balancedString(self, s: str) -> int:
        total_count, window_count, seen = Counter(s), Counter(), set()
        n = len(s)
        min_length = n
        k = n // 4
        if self.isStringBalanced(window_count, total_count, k):
            return 0

        start = end = 0
        while start < len(s) and end < len(s):
            if end not in seen:
                window_count[s[end]] += 1
                seen.add(end)
            
            if self.isStringBalanced(window_count, total_count, k):
                min_length = min(min_length, end - start + 1)
                window_count[s[start]] -= 1
                start += 1
            else:
                end += 1
        return min_length

    
    def isStringBalanced(self, window_count, total_count, k):
        """
        Checks if the string will be balanced after replacing the letters in the
        window by some letters
        """
        for letter, count_ in total_count.items():
            if count_ - window_count[letter] > k:
                return False
        return True