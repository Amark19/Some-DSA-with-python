class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(grid)
        n = len(grid[0])
        visited_arr = set()
        row_delta = [-1, 0, 1, 0]
        col_delta = [0, -1, 0, 1]

        def dfsTraverse(x, y):
            visited_arr.add((x, y))
            # grid[x][y] ="B" # b for border
            for delta in range(4):
                t_x = x + row_delta[delta]
                t_y = y + col_delta[delta]
                if t_x >= 0 and t_y >= 0 and t_x < m and t_y < n and (t_x, t_y) not in visited_arr and grid[t_x][
                    t_y] == "O":
                    dfsTraverse(t_x, t_y)

        for i in range(m):
            if (i, 0) not in visited_arr and grid[i][0] == 'O':  # Left border
                dfsTraverse(i, 0)
            if (i, n - 1) not in visited_arr and grid[i][n - 1] == 'O':  # Right border
                dfsTraverse(i, n - 1)
        for i in range(n):
            if (0, i) not in visited_arr and grid[0][i] == 'O':  # up border
                dfsTraverse(0, i)
            if (m - 1, i) not in visited_arr and grid[m - 1][i] == 'O':  # bottom border
                dfsTraverse(m - 1, i)
        ## run for middle elements
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O" and (i, j) not in visited_arr:
                    grid[i][j] = 'X'