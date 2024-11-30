class Solution:
    def intervalIntersection(self, firstList, secondList):
        n, m = len(firstList), len(secondList)
        if n == 0 or m == 0:
            return []
        answer = []

        i = j = 0
        while i < n and j < m:
            s1, s2 = firstList[i][0], secondList[j][0]
            e1, e2 = firstList[i][1], secondList[j][1]
            
            # If there is an intersection
            if s1 <= s2 and e1 >= s2:
                answer.append([s2, min(e1, e2)])
            elif s1 >= s2 and e2 >= s1:
                answer.append([s1, min(e1, e2)])
            
            if e1 > e2:
                j += 1
            else:
                i += 1
        
        return answer