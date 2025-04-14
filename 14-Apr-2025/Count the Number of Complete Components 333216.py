# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False for _ in range(n)]
        total_edges = 0
        nodes = 0
        def dfs(node):
            nonlocal total_edges
            nonlocal nodes

            nodes += 1
            total_edges += len(graph[node])
            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                if total_edges == nodes * (nodes - 1):
                    components += 1
                nodes = 0
                total_edges = 0
        return components

