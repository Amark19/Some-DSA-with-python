from collections import defaultdict


class graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def travserse(self, node, q, visited):
        del q[0]
        for val in self.graph[node]:
            # if val not in visited:
            q.append(val)
            # if val not in visited:
            #     visited.add(val)
            #     self.travserse(val, q, visited)
            # else:
            #     return visited 
        visited.add(node)
        self.travserse(q[0],q,visited)
        return visited


g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
q = []
q.append(0)
visited = set()
print(g.travserse(0, q, visited))
# 0,1
# 0,2
