obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
m = len(obstacleGrid)
n = len(obstacleGrid[0])
temp = [-1 for _ in range(n)]
for i in range(m):
    dp = [-1 for _ in range(n)]
    for j in range(n):
        if i < 0 or j < 0: dp[j] = 0;continue
        if obstacleGrid[i][j] == 1:dp[j] = 0;continue
        if i==0 and j==0:dp[j] = 1;continue
        up,left = 0,0
        if i>0:up = temp[j]
        if j>0:left = dp[j-1]
        dp[j] = up + left
    temp = dp.copy()
print( temp[n-1])