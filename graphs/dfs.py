from collections import defaultdict
class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,src,dest):
        self.graph[src].append(dest)
    def travserse(self,node,visited):
        visited.add(node)
        for val in self.graph[node]:
            if val not in visited:
                self.travserse(val,visited)
            else:
                return visited
        return visited


g = graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,4)
g.addEdge(2,3)
g.addEdge(3,4)
#{0:[1,2],1:[4],2:[3],3:{4}}
visited = set()
print(g.travserse(0,visited))
#0,1
#0,2