class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isok(row,col,board,n):
            temp_r,temp_c = row,col
            ##check top left
            while row >= 0 and col >=0:
                if board[row][col] == 'Q':return False
                row-=1
                col-=1
            
            #check left
            row,col = temp_r,temp_c
            while col >= 0:
                if board[row][col] == 'Q':return False
                col-=1

            #check bottom left
            row,col = temp_r,temp_c
            while row < n and col >=0:
                if board[row][col] == 'Q':return False
                row+=1
                col-=1
            return True
        def tosolve(col,board):
            if col == n:##that means till n-1 column it got perfect board now trying to find solution for next (n - 1 )+ 1 column (already solved)
                ans.append([''.join(board[i].copy()) for i in range(n)])
                return
            for row in range(n):
                if isok(row,col,board,n):
                    board[row][col] = 'Q'
                    tosolve(col+1,board)
                    board[row][col] = '.'
        ans = []
        board = [['.' for _ in range(n)]for _ in range(n)]
        tosolve(0,board)
        return ans
