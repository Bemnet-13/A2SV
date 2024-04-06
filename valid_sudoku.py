class Solution:
    def isValidSudoku(self, board) -> bool:
        for row in board:
            res = self.sudokuChecker(row)
            if not res:
                return res
        cols = []
        for i in range(9):
            new_col = []
            for j in range(9):
                new_col.append(board[j][i])
            cols.append(new_col)
        for col in cols:
            res = self.sudokuChecker(col)
            if not res:
                return res
        
        # check 3 *3 matrix
        for off_x in range(0, 9, 3):           
            for off_y in range(0, 9, 3):
                sub_board = []
                for i in range(3):
                    for j in range(3):
                        sub_board.append(board[i + off_x][j + off_y])

                res = self.sudokuChecker(sub_board)
                if not res :
                    return res
        
        return True       
    
    def sudokuChecker(self, lst):
        blank = {}
        for elem in lst:
            if elem not in blank:
                blank[elem] = 1
            elif elem != ".":
                return False
        return True

trial = Solution()
o = trial.isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
