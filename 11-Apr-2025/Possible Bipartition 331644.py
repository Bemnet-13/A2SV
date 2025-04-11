# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        
        colors = [-1] * n
        ans = True
        def dfs(node, color):

            nonlocal colors
            nonlocal ans
            colors[node - 1] = color
            for neighbor in graph[node]:
                if colors[neighbor - 1] == -1:
                    dfs(neighbor, color ^ 1)
                elif colors[neighbor - 1] == color:
                    ans = False
            
        for i in range(1, n + 1):
            if colors[i - 1] == -1:
                dfs(i, 0)
        return ans