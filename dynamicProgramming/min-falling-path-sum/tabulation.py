def minFallingPathSum(matrix) -> int:
    n = len(matrix)
    dp = [[-1 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        dp[0][i] = matrix[0][i]
    for i in range(1, n):
        for j in range(n):
            left, right = float("inf"), float("inf")
            if j > 0: left = matrix[i][j] + dp[i - 1][j - 1]
            up = matrix[i][j] + dp[i - 1][j]
            if j < n - 1: right = matrix[i][j] + dp[i - 1][j + 1]
            dp[i][j] = min(left, up, right)
    return min(dp[n - 1])


print(minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))  # 13