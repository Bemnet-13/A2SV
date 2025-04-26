# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)
        
        ans = [set() for _ in range(numCourses)]
        colors = [0 for _ in range(numCourses)]

        def dfs(node, curr):
            nonlocal ans
            nonlocal colors

            colors[node] = 1

            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    ans[neighbor].add(curr)
                    dfs(neighbor, curr)

        for i in range(numCourses):
            dfs(i, i)
            colors = [0 for _ in range(numCourses)]

        res = []
        for u, v in queries:
            res.append(u in ans[v])
            
        return res