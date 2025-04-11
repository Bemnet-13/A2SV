# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)

        ans = True
        def dfs(node, color):
            nonlocal colors
            nonlocal ans

            colors[node] = color
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    c = 1 if color == 0 else 0
                    dfs(neighbor, c)

                elif colors[neighbor] == color:
                    ans = False
            
        
        for i in range(len(graph)):
            
            if colors[i] == -1:
                dfs(i, 0)

        return ans