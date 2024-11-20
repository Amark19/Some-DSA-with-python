class Solution:
    timer = 1

    def dfs(self, vis, parent, node, adj, time_arr, low_arr, bridges):
        vis.add(node)
        time_arr[node] = low_arr[node] = self.timer
        self.timer += 1
        for val in adj[node]:
            if val == parent: continue
            if val not in vis:
                self.dfs(vis, node, val, adj, time_arr, low_arr, bridges)
                low_arr[node] = min(low_arr[val], low_arr[node])
                # is there a bridge ?
                # 8(8|6) -> 10(10|10)
                # so there is no way except for 10 to reach 8 than 8 <-> 10 so there is a bridge
                # that means child low counter should be greater than parent time of insertion one (while backtracking)
                if low_arr[val] > time_arr[node]:
                    bridges.append([node, val])
            else:
                low_arr[node] = min(low_arr[val], low_arr[node])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for i in range(len(connections)):
            u = connections[i][0]
            v = connections[i][1]
            adj[u].append(v)
            adj[v].append(u)
        time_arr = list(range(n))
        low_arr = list(range(n))
        bridges = []
        vis = set()
        self.dfs(vis, -1, 0, adj, time_arr, low_arr, bridges)
        return bridges
