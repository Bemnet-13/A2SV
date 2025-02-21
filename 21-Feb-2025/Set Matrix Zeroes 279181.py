# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        
        for row, col in zeros:
            for c in range(len(matrix[0])):
                matrix[row][c] = 0
            for r in range(len(matrix)):
                matrix[r][col] = 0