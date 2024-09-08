def isCyclic(V: int, adj) -> bool:
    indegree = V * [0]
    for v in range(V):
        for node in adj[v]:
            indegree[node] += 1
    q = []
    cnt = 0
    for v in range(V):
        if indegree[v] == 0: q.append(v)
    while q:
        node = q[0]
        del q[0]
        cnt += 1
        for nd in adj[node]:
            indegree[nd] -= 1
            if indegree[nd] == 0:
                q.append(nd)
    if cnt != V:
        return True
    return False

"""
Explanation:
 Why cnt != V?
 
 Ideally topological sort only works for DAG(Directed Acyclic Graphs). If the graph has a cycle, 
 then the indegree of the node in the cycle will never be 0. So, the node will never be added to the queue. 
 So, the count of the nodes that are added to the queue will be less than the total number of nodes in the graph. 
 So, if cnt != V, then the graph has a cycle.
"""