# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        queue = deque([(sr, sc)])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]
        visited[sr][sc] = True

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        while queue:
            r, c = queue.popleft()
            original_color = image[r][c]           
            image[r][c] = color

            for i, v in directions:
                nr, nc = r + i, c + v
                if inbound(nr, nc) and not visited[nr][nc] and image[nr][nc] == original_color:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return image