class Solution:
    def rotate(self, matrix) -> None:
        copy = [row[:] for row in matrix]

        for i in range(0, len(matrix)):
            for j in range(len(matrix)-1, -1, -1):
                matrix[i][len(matrix) -j - 1] = copy[i][j]
        