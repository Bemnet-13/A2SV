# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        rows, cols = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        total_oranges = 0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    total_oranges += 1
                
                if grid[i][j] == 2:
                    queue.append((i, j, minute))
        
        rotten = len(queue)
        while queue:      
            if rotten == total_oranges:
                return minute
            while queue and queue[0][2] == minute:
                x, y, minute_ = queue.popleft()
                for r, c in dirs:
                    if 0 <= x + r < rows and 0 <= y + c < cols and grid[x + r][y + c] == 1:
                        queue.append((x + r, y + c, minute_ + 1))
                        grid[x + r][y + c] = 2
                        rotten += 1     

            minute += 1
        
        return -1 if rotten < total_oranges else minute