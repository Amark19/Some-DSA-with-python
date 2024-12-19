def cherryPickup(grid):
    rows = len(grid)
    cols = len(grid[0])

    def recur(i, j1, j2):
        if j1 < 0 or j2 < 0 or j2 > cols - 1 or j1 > cols - 1:
            return 0
        if i == rows - 1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]
        mx = 0
        for d1 in range(-1, 2):
            for d2 in range(-1, 2):
                value = 0
                if j1 == j2:
                    value = grid[i][j2]
                else:
                    value = grid[i][j1] + grid[i][j2]
                value += recur(i + 1, j1 + d1, j2 + d2)
                mx = max(mx, value)
        return mx

    return recur(0, 0, cols - 1)


print(cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5]]))
