# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        RED, BLUE = 0, 1

        for a, b in redEdges:
            graph[a].append((b, RED))
        
        for u, v in blueEdges:
            graph[u].append((v, BLUE))
        
        queue = deque([(0, RED), (0, BLUE)])
        ans = [-1] * n
        level = 0
        visited = set()

        while queue:
            # print(queue, level)
            for _ in range(len(queue)):
                node, color = queue.popleft()
                visited.add((node, color))
                if ans[node] == -1:
                    ans[node] = level
                neighbor_color = color ^ 1
                for neighbor in graph[node]:
                    if neighbor[1] == neighbor_color and (neighbor[0], neighbor_color) not in visited:
                        queue.append((neighbor[0],  neighbor_color))

            level += 1

        return ans