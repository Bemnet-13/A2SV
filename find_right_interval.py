class Solution:
    def findRightInterval(self, intervals):

        sorted_intervals = sorted(intervals, key = lambda i : i[0])
        right_intervals = ["x"] * len(intervals)
        for i in range(len(sorted_intervals)):
            start, end = sorted_intervals[i][0], sorted_intervals[i][1]
            l , r = i, len(sorted_intervals) - 1
            while l < r:
                mid = (l + r) // 2
                if sorted_intervals[mid][0] >= end:
                    r = mid
                else:
                    l = mid + 1
            
            x = intervals.index(sorted_intervals[i])
            if l < len(intervals) and end <= sorted_intervals[l][0]:
                p = intervals.index(sorted_intervals[l])
            else:
                p = -1
            right_intervals[x] = p
        
        return right_intervals