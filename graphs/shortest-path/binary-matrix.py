class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        n = len(grid)
        dist_arr = [[float("inf") for _ in range(n)] for _ in range(n)]
        dist_arr[0][0] = 0
        que = [(0, (0, 0))]
        row_delta = [-1, -1, -1, 0, 1, 1, 1, 0]
        col_delta = [-1, 0, 1, -1, -1, 0, 1, 1]
        while que:
            curr_dist, node = que[0]
            x, y = node
            del que[0]
            for delta in range(8):
                t_x = x + row_delta[delta]
                t_y = y + col_delta[delta]
                curr_node = (t_x, t_y)
                if t_x >= 0 and t_y >= 0 and t_x < n and t_y < n:
                    wt = grid[t_x][t_y]
                    if dist_arr[t_x][t_y] > dist_arr[x][y] + 1 and wt == 0:
                        dist_arr[t_x][t_y] = dist_arr[x][y] + 1
                        que.append((dist_arr[t_x][t_y], curr_node))
        if dist_arr[n - 1][n - 1] == float("inf"): return -1
        return dist_arr[n - 1][n - 1] + 1