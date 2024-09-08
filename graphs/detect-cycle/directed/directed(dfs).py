class Solution:
    def traverse(self, adj, node, visited_arr, path_arr):
        # if node in
        visited_arr.add(node)
        path_arr.add(node)
        for val in adj[node]:
            if val not in visited_arr:
                if self.traverse(adj, node, val, visited_arr, path_arr):
                    return True
            elif val in path_arr:
                return True
        path_arr.remove(node)
        return False

    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:

        # Code here
        visited_arr = set()
        path_arr = set()
        for val in range(V):
            if val not in visited_arr:
                if self.traverse(adj, val, visited_arr, path_arr):
                    return True
        return False
        # code here


"""
Maintaining a path array to keep track of the nodes that are part of the current path.
If we reach a node that is already part of the path, then there is a cycle.

example:
     1
    / \
   2 - 3
   
we start at 1, we add 1 in visited_arr and path_arr
then we go to 2, we add 2 in visited_arr and path_arr
then we go to 3, we add 3 in visited_arr and path_arr
then we go to 1, we find 1 in path_arr, so there is a cycle
"""