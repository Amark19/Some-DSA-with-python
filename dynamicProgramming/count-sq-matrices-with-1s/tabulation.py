class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            dp[r][0] = matrix[r][0]
        for c in range(col):
            dp[0][c] = matrix[0][c]
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c]:
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
        return sum([sum(dp[p]) for p in range(row)])