from typing import List


class Solution:
    def traverse(self, adj, parent, node, visited_arr):
        # if node in
        visited_arr.add(node)
        for val in adj[node]:
            if val not in visited_arr:
                if self.traverse(adj, node, val, visited_arr):
                    return True
            elif val != parent:
                return True
        return False

        # Function to detect cycle in an undirected graph.
        def isCycle(self, V: int, adj: List[List[int]]) -> bool:

            # Code here
            visited_arr = set()
            for val in range(V):
                if val not in visited_arr:
                    if self.traverse(adj, -1, val, visited_arr):
                        return True
            return False