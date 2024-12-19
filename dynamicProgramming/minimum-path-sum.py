class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = [[float("inf")] * (col + 1) for i in range(row + 1)]
        res[row - 1][col] = 0

        for r in range(row - 1, -1, -1):
            for c in range(col - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        return res[0][0]
