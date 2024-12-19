class Solution:
    # Code here
    def traverse(self, adj, node, visited_arr, st):
        # if node in
        visited_arr.add(node)
        for val in adj[node]:
            if val not in visited_arr:
                self.traverse(adj, val, visited_arr, st)
        st.append(node)

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        visited_arr = set()
        st = []
        for val in range(V):
            if val not in visited_arr:
                self.traverse(adj, val, visited_arr, st)
        return st[::-1]
