class Solution:
    def intervalIntersection(self, firstList, secondList):
        p1 = p2 = 0
        solution = []
        while p1 < len(firstList) and p2 < len(secondList):
            l1, r1 = firstList[p1] 
            l2, r2 = secondList[p2]
            set1= set(range(l1, r1 + 1))
            set2 = set(range(l2, r2 + 1))
            intersection = set1.intersection(set2)

            if intersection != set():
                solution.append([min(intersection) , max(intersection)])
            
            if p2 + 1 < len(secondList) and firstList[p1][1] >= secondList[p2 + 1][0]:
                p2 += 1
            elif p2 + 1 < len(secondList) and secondList[p2][1] >= firstList[p1 + 1][0]:
                p1 += 1
            else:
                p1 += 1
                p2 += 1
        return solution

trial = Solution()
o = trial.intervalIntersection(firstList = [[1,3],[5,9]], secondList = [])
print(o)   