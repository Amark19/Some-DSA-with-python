class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def isvalid(val,row,col,board):
            for i in range(9):
                if board[row][i] == val:
                    return False
                if board[i][col] == val:
                    return False
                if board[3*(row//3) + i //3][3*(col//3) + i%3] == val:#check for particular 3x3 sub-boxes
                    return False
            return True
        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for val in range(1,10):
                            if isvalid(str(val),i,j,board):
                                board[i][j] = str(val)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True
        solve(board)
