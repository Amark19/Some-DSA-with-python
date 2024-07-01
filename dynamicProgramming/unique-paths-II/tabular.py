def uniquePathsWithObstacles(obstacleGrid) -> int:
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i < 0 or j < 0: dp[i][j] = 0;continue
            if obstacleGrid[i][j] == 1:dp[i][j] = 0;continue
            if i==0 and j==0:dp[i][j] = 1;continue
            up,left = 0,0
            if i>0:up = dp[i-1,j]
            if j>0:left = dp[i,j-1]
            dp[i][j] = up + left
    return dp[m-1][n-1]

print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])) # 2