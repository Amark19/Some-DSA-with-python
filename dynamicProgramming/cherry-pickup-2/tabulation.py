def cherryPickup(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = [[[-1 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]
    ## BASE CASE
    for j1 in range(0, cols):
        for j2 in range(0, cols):
            if j1 == j2:
                dp[rows - 1][j1][j2] = grid[rows - 1][j1]
            else:
                dp[rows - 1][j1][j2] = grid[rows - 1][j1] + grid[rows - 1][j2]
    ## BASE CASE ENDS

    for i in range(rows - 2, -1, -1):
        for j in range(0, cols):
            for k in range(0, cols):
                mx = 0
                for d1 in range(-1, 2):
                    for d2 in range(-1, 2):
                        value = 0
                        if j == k:
                            value = grid[i][k]
                        else:
                            value = grid[i][j] + grid[i][k]
                        if j + d1 >= 0 and j + d1 < cols and k + d2 >= 0 and k + d2 < cols:
                            value += dp[i + 1][j + d1][k + d2]
                        mx = max(mx, value)
                dp[i][j][k] = mx
    return dp[0][0][cols - 1]


print(cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5]]))