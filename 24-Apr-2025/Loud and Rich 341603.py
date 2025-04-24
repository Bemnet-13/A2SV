# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        n = len(quiet)
        quietness_map = {quiet[i] : i for i in range(n)}

        for a, b in richer:
            graph[b].append(a)
        
        colors = [0 for _ in range(n)]

        for person in range(n):
            if colors[person] == 0:
                self.topSort(person, graph, colors, quiet)
        ans = [-1 for _ in range(n)]
        for i in range(n):
            ans[i] = quietness_map[quiet[i]]

        return ans
        
    def topSort(self, node, graph, colors, quiet):
        
        colors[node] = 1

        for neighbor in graph[node]:
            if colors[neighbor] == 0:
                max_quiet_richer = self.topSort(neighbor, graph, colors, quiet)
                quiet[node] = min(quiet[node], max_quiet_richer)
            else:
                quiet[node] = min(quiet[node], quiet[neighbor])
        
        colors[node] = 2
        return quiet[node]