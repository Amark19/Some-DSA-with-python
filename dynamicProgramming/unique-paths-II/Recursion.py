def uniquePathsWithObstacles(obstacleGrid) -> int:
    def recur(arr, i, j):
        if i == 0 and j == 0: return 1
        if i < 0 or j < 0: return 0
        if arr[i][j] == 1: return 0
        up = recur(arr, i - 1, j)
        left = recur(arr, i, j - 1)
        return up + left

    i = len(obstacleGrid)
    j = len(obstacleGrid[0])
    return recur(obstacleGrid, i - 1, j - 1)


print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
