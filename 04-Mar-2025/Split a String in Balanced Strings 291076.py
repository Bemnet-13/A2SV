# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        count_l = count_r = 0

        for letter in s:
            if letter == 'R': count_r += 1
            if letter == 'L': count_l += 1

            if count_r == count_l:
                ans += 1
                count_r = count_l = 0
        
        return ans