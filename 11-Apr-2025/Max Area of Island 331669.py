# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        area = 0
        def dfs(i, j):
            nonlocal visited
            visited[i][j] = True
            nonlocal area
            area += 1

            for x_inc, y_inc in directions:
                new_x = i + x_inc
                new_y = j + y_inc
                if inbound(new_x, new_y) and not visited[new_x][new_y] and grid[new_x][new_y]:
                    dfs(new_x, new_y)
            
        
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and grid[i][j] not in visited:
                    dfs(i, j)
                    max_area = max(max_area, area)
                    area = 0
        
        return max_area