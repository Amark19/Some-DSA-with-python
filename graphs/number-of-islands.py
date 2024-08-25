class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited_arr = set()
        row_delta = [-1, 0, 1, 0]
        col_delta = [0, -1, 0, 1]

        def dfsTraverse(grid, visited_arr, node):
            x, y = node
            visited_arr.add(node)
            for delta in range(4):
                t_x = x + row_delta[delta]
                t_y = y + col_delta[delta]
                if t_x >= 0 and t_y >= 0 and t_x < m and t_y < n and (t_x, t_y) not in visited_arr and grid[t_x][
                    t_y] == "1":
                    dfsTraverse(grid, visited_arr, (t_x, t_y))

        cnt = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited_arr and grid[i][j] == "1":
                    dfsTraverse(grid, visited_arr, (i, j))
                    cnt += 1
        return cnt