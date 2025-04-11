# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(set)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)
        
        visited = [False for _ in range(n)]

        def dfs(node):
            nonlocal visited
            visited[node] = True

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        
        provinces = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1
        
        return provinces