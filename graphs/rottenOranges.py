class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = []
        visited_arr = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        cntFresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    visited_arr[i][j] = 1
                    que.append([(i, j), 0])
                elif grid[i][j] == 1:
                    cntFresh += 1
        row_delta = [-1, 0, 1, 0]
        col_delta = [0, -1, 0, 1]
        tmx = 0
        cnt_rotten = 0
        while len(que) > 0:
            x, y = que[0][0]
            t = que[0][1]
            tmx = max(t, tmx)
            for i in range(4):
                t_x = x + row_delta[i]
                t_y = y + col_delta[i]
                if t_x >= 0 and t_y >= 0 and t_x < len(grid) and t_y < len(grid[0]) and visited_arr[t_x][t_y] != 1 and \
                        grid[t_x][t_y] == 1:
                    que.append([(t_x, t_y), t + 1])
                    visited_arr[t_x][t_y] = 1
                    cnt_rotten += 1
            del que[0]
        if cnt_rotten != cntFresh: return -1
        return tmx

## BFS