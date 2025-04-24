# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0 for _ in range(len(graph))]
        safe = []

        for node in range(len(graph)):
            if colors[node] == 0:
                self.topSort(node, colors, graph, safe)
        
        return sorted(safe)
        

    def topSort(self, node, colors, graph, safe):
        if colors[node] == 1:
            return False
        
        colors[node] = 1

        for neighbor in graph[node]:
            if colors[neighbor] == 2:
                continue
            
            if not self.topSort(neighbor, colors, graph, safe) == 1:
                return False
        
        safe.append(node)
        colors[node] = 2
        return True