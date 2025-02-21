# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point: point[0])
        max_area = 0

        for i in range(len(points) - 1):
            area = points[i + 1][0] - points[i][0]
            max_area = max(max_area, area)

        return max_area
            