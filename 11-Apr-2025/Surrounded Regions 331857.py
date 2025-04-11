# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        c_visited = [[False] * m for _ in range(n)]

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        def on_edge(i, j):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                return True
            return False 

        surrounded = True
        def explore(i, j):
            nonlocal surrounded
            nonlocal visited
            visited[i][j] = True
            for dx, dy in directions:
                new_r = i + dx
                new_c = j + dy
                
                if not inbound(new_r, new_c):
                    surrounded = False
                if inbound(new_r, new_c):
                    if not visited[new_r][new_c] and board[new_r][new_c] == "O":
                        explore(new_r, new_c)
               

        def change(i, j):    
            nonlocal c_visited
            c_visited[i][j] = True
            board[i][j] = 'X'


            for dx, dy in directions:
                new_r = i + dx
                new_c = j + dy
                if inbound(new_r, new_c):
                    if not c_visited[new_r][new_c] and board[new_r][new_c] == "O":
                        change(new_r, new_c)
                
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and board[i][j] == "O":
                    if not on_edge(i, j):
                        explore(i, j)
                        if surrounded:
                            change(i, j)
                surrounded = True
        
        return board