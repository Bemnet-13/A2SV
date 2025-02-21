# Problem: Number of Times Binary String Is Prefix-Aligned - https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

class Solution:
    def numTimesAllBlue(self, flips) -> int:
        count = total = 0
        max_ = 0
        for num in flips:
            total += num
            max_ = max(max_, num)
            if (max_*(max_+1)) // 2 == total:
                count += 1
        return count
