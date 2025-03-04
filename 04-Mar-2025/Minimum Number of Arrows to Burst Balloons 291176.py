# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda point : point[1])
        curr = 0
        ans = 1

        for i in range(1, len(points)):
            if points[curr][1] < points[i][0]:
                ans += 1
                curr = i
        
        return ans