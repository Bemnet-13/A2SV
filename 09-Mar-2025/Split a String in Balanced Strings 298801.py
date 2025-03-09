# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        counter = Counter()

        for letter in s:
            counter[letter] += 1

            if counter['L']== counter['R']:
                ans += 1
                counter['L'] = counter['R'] = 0
        
        return ans