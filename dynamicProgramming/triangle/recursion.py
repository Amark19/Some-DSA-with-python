def minimumTotal(triangle) -> int:
    n = len(triangle)
    def recur(i, j):
        if i == n - 1:return triangle[n-1][j]
        down = triangle[i][j] + recur(i+1,j+1)
        down_right = triangle[i][j] + recur( i+1, j)
        return min(down,down_right)
    return recur(0,0)