# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = [[0, 0] for i in range(1, n + 1)]

        for u, v in trust:
            pos = u - 1
            graph[pos][0] += 1
            graph[v - 1][1] += 1
        
        for i in range(len(graph)):
            out, in_ = graph[i]
            if out == 0 and in_ == n - 1:
                return i + 1
        
        return -1