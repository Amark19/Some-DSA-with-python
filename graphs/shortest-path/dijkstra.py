from typing import List
import heapq


class Solution:

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
        que = [(0, S)]
        dist_arr = [float("inf") for _ in range(V)]
        dist_arr[S] = 0
        while que:
            curr_dist, node = heapq.heappop(que)
            for val in adj[node]:
                curr_node = val[0]
                wt = val[1]
                if dist_arr[curr_node] > dist_arr[node] + wt:
                    dist_arr[curr_node] = dist_arr[node] + wt
                    heapq.heappush(que, (dist_arr[curr_node], curr_node))

        return dist_arr


sol = Solution()
# run on this test case A → B (4), A → C (2), B → C (-3)
print(sol.dijkstra(3, [[[1, 4], [2, 2]], [[2, -3]], []], 0))  # [0, 1, -2]
