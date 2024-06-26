class Solution:
    def maxWidthOfVerticalArea(self, points) -> int:
        points.sort(key = lambda point : point[0])

        max_area = 0
        for i in range(len(points)-1):
            max_area = max(max_area, points[i+1][0] - points[i][0])
        
        return max_area
    
