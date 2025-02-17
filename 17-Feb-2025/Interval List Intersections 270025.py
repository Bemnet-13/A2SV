# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        ans = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            l1, r1 = firstList[i]
            l2, r2 = secondList[j]

            if r1 < r2:
                if l2 <= r1:
                    ans.append([max(l1, l2), r1])
                i += 1
            elif r1 == r2:
                ans.append([max(l1, l2), r1])
                i += 1
                j += 1
            else:
                if l1 <= r2:
                    ans.append([max(l1, l2), r2])
                j += 1
        
        return ans

