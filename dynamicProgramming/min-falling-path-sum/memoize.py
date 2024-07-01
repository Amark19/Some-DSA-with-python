def minFallingPathSum(matrix) -> int:
    n = len(matrix)
    dp = [[-1 for i in range(n)] for j in range(n)]

    def recur(i, j):
        if i < 0 or j < 0: return float("inf")
        if i > n - 1 or j > n - 1: return float("inf")
        if i == 0: return matrix[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        left = matrix[i][j] + recur(i - 1, j - 1)
        up = matrix[i][j] + recur(i - 1, j)
        right = matrix[i][j] + recur(i - 1, j + 1)
        dp[i][j] = min(left, up, right)
        return dp[i][j]

    x = float("inf")
    for i in range(1, n + 1):
        x = min(x, recur(n - 1, n - i))
    return x