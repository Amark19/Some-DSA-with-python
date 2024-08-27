class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # If u read bipartite defination in wikipedia it mentioned two things
        # 1. Whatever written in problem description
        # 2. Coloring the vertex with alternate color & if we find two adjacent vertex with same color then
        # it is not bipartite graph

        m = len(graph)
        n = len(graph[0])
        visited_arr = {}

        def checkBipartite(visited_arr, start_node):
            que = []
            que.append(start_node)
            visited_arr[start_node] = 0
            while len(que) > 0:
                node = que[0]
                for val in graph[node]:
                    if val not in visited_arr:
                        que.append(val)
                        visited_arr[val] = 1 - visited_arr[node]
                    elif visited_arr[val] == visited_arr[node]:
                        return False
                del que[0]
            return True

        # check for unconnected components
        for i in range(m):
            if i not in visited_arr:
                if checkBipartite(visited_arr, i) == False:
                    return False
        return True