def minFallingPathSum(matrix) -> int:
    n = len(matrix)

    def recur(i, j):
        if i < 0 or j < 0: return float("inf")
        if i > n - 1 or j > n - 1: return float("inf")
        if i == 0: return matrix[i][j]
        left = matrix[i][j] + recur(i - 1, j - 1)
        up = matrix[i][j] + recur(i - 1, j)
        right = matrix[i][j] + recur(i - 1, j + 1)
        return min(left, up, right)
    x = float("inf")
    for i in range(1, n + 1):
        x = min(x,recur(n - 1, n - i))
    return x