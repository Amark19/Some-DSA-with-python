def uniquePathsWithObstacles(obstacleGrid) -> int:
    i = len(obstacleGrid)
    j = len(obstacleGrid[0])
    dp = [[-1 for _ in range(j)] for _ in range(i)]

    def recur(arr, i, j):
        if i < 0 or j < 0: return 0
        if arr[i][j] == 1: return 0
        if i == 0 and j == 0: return 1
        if dp[i][j] != -1: return dp[i][j]
        up = recur(arr, i - 1, j)
        left = recur(arr, i, j - 1)
        dp[i][j] = up + left
        return dp[i][j]

    return recur(obstacleGrid, i - 1, j - 1)
