from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        directions = [(1,0), (0,1), (-1, 0), (0, -1), (1, 1), (1,-1), (-1, 1), (-1, -1)]
        n = len(grid)
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n

        queue = deque([0, 0])
        path = 1

        if grid[0][0] == 1:
            return -1

        while queue:
            path += 1
            
            for _ in range(len(queue)):
                if not queue:
                    return path 
                curr_col = queue.popleft()
                curr_row = queue.popleft()
                if curr_col == n - 1 and curr_row  == n - 1 and grid[curr_row][curr_col] == 0:
                    return path
                elif curr_col == n - 1 and curr_row  == n - 1:
                    return -1
                for x, y in directions:
                    new_row = curr_row + x
                    new_col = curr_col + y
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                        queue.append(new_row)
                        queue.append(new_col)
                        grid[new_row][new_col] = 1
        return -1

tr = Solution()
o = tr.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
print(o)