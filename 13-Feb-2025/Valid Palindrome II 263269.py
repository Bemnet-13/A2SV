# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.palindromeChecker(s, True) | self.palindromeChecker(s, False)
    
    def palindromeChecker(self, s, fromRight):
        left = 0
        right = len(s) - 1
        mismatch_count = 0

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif mismatch_count == 0:
                if fromRight:
                    right -= 1
                else:
                    left += 1
                mismatch_count += 1
            elif mismatch_count > 0:
                return False
        
        return True