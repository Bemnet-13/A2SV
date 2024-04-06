class Solution:
    def countUnguarded(self, m: int, n: int, guards, walls) -> int:
        grid = [[0] * n for _ in range(m)]

        for x , y in guards:
            grid[x][y] = "G"
        
        for x , y in walls:
            grid[x][y] = "W"

        
        
Solution().countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])