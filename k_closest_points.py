class Solution:
    def kClosest(self, points, k: int):
        def sorter(point):
            return point[0]**2 + point[1]**2
        
        points.sort(key = sorter)
        return points[:k]
        
trial = Solution()
o = trial.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)
print(o)