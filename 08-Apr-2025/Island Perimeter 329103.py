# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        ans = 0
        def dfs(visited, row, col, prev):

            visited[row][col] = True
            nonlocal ans

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if not inbound(new_row, new_col):
                    ans += 1
                elif inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                    ans += 1
             

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if inbound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col] == 1:
                    dfs(visited, new_row, new_col, (row, col))
                
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    dfs(visited, i, j, None)
                    return ans
        
        return ans