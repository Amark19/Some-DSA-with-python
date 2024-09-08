class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def traverse(adj, node, visited_arr, path_arr, safe_nodes_map):
            # if node in
            visited_arr.add(node)
            path_arr.add(node)
            for val in adj[node]:
                if val not in visited_arr:
                    if traverse(adj, val, visited_arr, path_arr, safe_nodes_map):
                        return True
                elif val in path_arr:
                    return True
            safe_nodes_map.add(node)
            path_arr.remove(node)
            return False

        # Code here
        visited_arr = set()
        path_arr = set()
        safe_nodes_map = set()
        for val in range(len(graph)):
            if val not in visited_arr:
                traverse(graph, val, visited_arr, path_arr, safe_nodes_map)
        return sorted(list(safe_nodes_map))