def shortestPath(self, edges, n, m, src):
    # code here
    # create adj
    adj = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge[0], edge[1]
        adj[u].append(v)
        adj[v].append(u)
    dist = [float("inf") for _ in range(n)]
    dist[src] = 0
    que = [src]
    while que:
        node = que[0]
        del que[0]
        for val in adj[node]:
            if dist[val] > dist[node] + 1:
                dist[val] = dist[node] + 1
                que.append(val)
    for i in range(n):
        if dist[i] == float('inf'):
            dist[i] = -1
    return dist
