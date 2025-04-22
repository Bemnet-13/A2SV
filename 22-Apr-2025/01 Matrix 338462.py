# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = set()

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        
        while queue:
            r, c = queue.popleft()

            for i, j in directions:
                nr, nc = r + i, c + j
                if inbound(nr, nc) and (nr, nc) not in visited:
                    queue.append((nr, nc))
                    visited.add((nr, nc))
                    mat[nr][nc] = mat[r][c] + 1
        
        return mat