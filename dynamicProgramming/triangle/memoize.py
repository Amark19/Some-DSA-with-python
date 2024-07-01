def minimumTotal(triangle) -> int:
    n = len(triangle)
    dp = [[-1 for _ in range(n)]for _ in range(n)]
    def recur(i, j):
        if i == n - 1:return triangle[n-1][j]
        if dp[i][j] != -1:return dp[i][j]
        down = triangle[i][j] + recur(i+1,j+1)
        down_right = triangle[i][j] + recur( i+1, j)
        dp[i][j] = min(down,down_right)
        return dp[i][j]
    return recur(0,0)