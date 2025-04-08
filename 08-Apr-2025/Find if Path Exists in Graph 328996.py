# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        ans = False

        def dfs(current):
            nonlocal seen
            nonlocal ans
            if current == destination:
                ans = True
                return
            
            seen.add(current)
            for neighbor in graph[current]:
                if neighbor not in seen and not ans:
                    dfs(neighbor)
        
        dfs(source)
        return ans
