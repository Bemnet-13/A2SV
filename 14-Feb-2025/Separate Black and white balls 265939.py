# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        # Check the fist invalid position
        left = 0
        while left < len(s):
            if s[left] == '1':
                break
            else:
                left += 1
        min_swaps = 0
        for right in range(left + 1, len(s)):
            # If the element at the right is 1, then swap it
            if s[right] == '0':
                min_swaps += right - left 
                left += 1
        
        return min_swaps