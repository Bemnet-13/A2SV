# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.ps = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                self.ps[i + 1][j + 1] = self.ps[i + 1][j] + self.ps[i][j + 1] - self.ps[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.ps[row2 + 1][col2 + 1] + self.ps[row1][col1] - self.ps[row1][col2 + 1] - self.ps[row2 + 1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)