def topoSort(V, adj):
    indegree = V * [0]
    for v in range(V):
        for node in adj[v]:
            indegree[node] += 1
    q = []
    top = []
    for v in range(V):
        if indegree[v] == 0: q.append(v)
    while q:
        node = q[0]
        del q[0]
        top.append(node)
        for nd in adj[node]:
            indegree[nd] -= 1
            if indegree[nd] == 0:
                q.append(nd)
    return top