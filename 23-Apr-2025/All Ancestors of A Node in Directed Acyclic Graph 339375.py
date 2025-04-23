# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        start = set([i for i in range(n)])
        for u, v in edges:
            graph[u].append(v)

        ans = [[] for _ in range(n)]
        
        def dfs(node, curr):        
            nonlocal ans
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:     
                    ans[neighbor].append(curr)
                    dfs(neighbor, curr)

        for i in range(n):
            visited = set()
            dfs(i, i)
        return ans