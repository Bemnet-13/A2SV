# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        pre_sum = sum([int(i) for i in s])
        curr_sum = 0

        max_score = len(s) - 1 - pre_sum 
        for i in range(len(s) - 1):
            curr_sum += int(s[i])
            max_score = max(max_score, i + 1 - curr_sum + pre_sum - curr_sum)

        return max_score