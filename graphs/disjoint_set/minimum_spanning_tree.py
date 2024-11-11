from disjoint_set import DisjointSet


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        edges = []
        # O(V+E)
        for node in range(len(adj)):
            for v, wt in adj[node]:
                edges.append([wt, node, v])
        ds_set = DisjointSet(V)
        # O(MlogM)
        edges.sort()  # sort by wt
        min_sp_wt = 0
        # O(M*4alpha)
        for edge in edges:
            wt = edge[0]
            u = edge[1]
            v = edge[2]
            if ds_set.find(u) != ds_set.find(v):
                ds_set.union_set(u, v)
                min_sp_wt += wt
        return min_sp_wt
