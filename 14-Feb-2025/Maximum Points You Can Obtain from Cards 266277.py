# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        cardPoints = cardPoints * 2
        curr_sum = sum(cardPoints[n - k : n - 1])
        max_sum = 0

        for i in range(n - 1, n + k):
            curr_sum += cardPoints[i]
            max_sum = max(max_sum, curr_sum)
            curr_sum -= cardPoints[i - k + 1]
        
        return max_sum