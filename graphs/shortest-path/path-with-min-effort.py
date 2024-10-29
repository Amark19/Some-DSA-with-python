class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dist_arr = [[float("inf") for _ in range(col)] for _ in range(row)]
        dist_arr[0][0] = 0
        que = [(0, (0, 0))]
        row_delta = [-1, 0, 1, 0]
        col_delta = [0, -1, 0, 1]
        while que:
            curr_dist, node = heapq.heappop(que)
            x, y = node
            if x == row - 1 and y == col - 1: return curr_dist
            for delta in range(4):
                t_x = x + row_delta[delta]
                t_y = y + col_delta[delta]
                curr_node = (t_x, t_y)
                if t_x >= 0 and t_y >= 0 and t_x < row and t_y < col:
                    wt = grid[t_x][t_y]
                    some_effort = max(abs(grid[x][y] - wt), dist_arr[x][y])
                    if some_effort < dist_arr[t_x][t_y]:
                        dist_arr[t_x][t_y] = some_effort
                        heapq.heappush(que, (some_effort, curr_node))
        return 0