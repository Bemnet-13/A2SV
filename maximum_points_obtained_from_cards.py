class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        points = sum(cardPoints[: k])
        max_points = points

        l = len(cardPoints) - 1
        r = k - 1
        while r >= 0:
            points += (cardPoints[l] - cardPoints[r])
            max_points = max(max_points, points)
            l -= 1
            r -= 1
        return max_points