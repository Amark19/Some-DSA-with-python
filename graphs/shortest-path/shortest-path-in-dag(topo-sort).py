class Solution:
    # O(v+e)
    def topoSort(self, v, st, vis, adj):
        vis.add(v)
        for val in adj[v]:
            if val[0] not in vis:
                self.topoSort(val[0], st, vis, adj)
        st.append(v)

    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            adj[u].append([v, wt])
        visited = set()
        st = []
        for i in range(n):
            if i not in visited:
                self.topoSort(i, st, visited, adj)
        short_arr = [float('inf')] * n
        short_arr[0] = 0
        st = st[::-1]
        # O(v+e)
        for val in st:
            for edge in adj[val]:
                node = edge[0]
                wt = edge[1]
                if short_arr[node] > short_arr[val] + wt:
                    short_arr[node] = short_arr[val] + wt

        for i in range(n):
            if short_arr[i] == float("inf"):
                short_arr[i] = -1
        return short_arr