from collections import defaultdict


class graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def travserse(self, node, queue, visited):
        if node in visited:
            return visited
        del queue[0]
        for val in self.graph[node]:
            queue.append(val)
        visited.add(node)
        self.travserse(queue[0], queue, visited)
        return visited


g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 4)
g.addEdge(2, 3)
g.addEdge(3, 4)
queue = []
queue.append(0)
visited = set()
print(g.travserse(0, queue, visited))
## level wise
# if graph is like this
# 0
# | \
# 1  2
# |   |
# 4   3
# |
# 5

# then output will be {0, (1, 2), (3, 4),5}