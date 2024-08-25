class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        visited_arr = set()
        row_delta = [-1, 0, 1, 0]
        col_delta = [0, -1, 0, 1]

        def dfsTraverse(grid, visited_arr, node):
            x, y = node
            pt_color = grid[x][y]
            visited_arr.add(node)
            grid[sr][sc] = color
            for delta in range(4):
                t_x = x + row_delta[delta]
                t_y = y + col_delta[delta]
                if t_x >= 0 and t_y >= 0 and t_x < m and t_y < n and (t_x, t_y) not in visited_arr and grid[t_x][
                    t_y] == pt_color:
                    dfsTraverse(grid, visited_arr, (t_x, t_y))
                    grid[t_x][t_y] = color

        dfsTraverse(grid, visited_arr, (sr, sc))
        return grid