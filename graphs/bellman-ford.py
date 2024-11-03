class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph,l
    '''

    def bellmanFord(self, V, edges, src):
        # code here
        max_dist = int(1e8)
        dist = [max_dist] * V
        dist[src] = 0
        for i in range(V - 1):
            for edge in edges:
                u = edge[0]
                v = edge[1]
                wt = edge[2]
                if dist[u] != max_dist and dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
        # check negative cycle by trying one more relaxation
        # As if there are at least one path which is not shorter then
        # that means there is a -ve cycle

        # If there is -ve cycle then values keep reducing
        for edge in edges:
            u = edge[0]
            v = edge[1]
            wt = edge[2]
            if dist[u] != max_dist and dist[u] + wt < dist[v]:
                return [-1]
        return dist