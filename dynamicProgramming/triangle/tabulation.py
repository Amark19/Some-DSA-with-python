def minimumTotal(triangle) -> int:
    n = len(triangle)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        dp[n - 1][j] = triangle[n - 1][j]
    for i in range(n - 2, -1, -1):
        for j in range(i, -1, -1):
            down = triangle[i][j] + dp[i + 1][j + 1]
            down_right = triangle[i][j] + dp[i + 1][j]
            dp[i][j] = min(down, down_right)
    return dp[0][0]