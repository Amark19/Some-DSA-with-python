class Solution:

    def dfs(self, vis, adj, st, val):
        # Standard DFS traversal to visit nodes
        # Marks the current node as visited
        vis.add(val)
        # Recursively visits all adjacent nodes that haven't been visited yet
        for ele in adj[val]:
            if ele not in vis:
                self.dfs(vis, adj, st, ele)
        # After all nodes in this component are visited, add this node to stack
        st.append(val)

    # Function to find the number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        """
        Steps for Kosaraju's Algorithm:
        1. Perform DFS on the original graph and keep track of the finishing order of nodes.
        2. Reverse the edges of the graph to create the transposed graph.
        3. Process nodes in the reverse order of finishing time to find strongly connected components.
        """

        # Step 1: Sort nodes by finishing times using DFS
        # `vis` set keeps track of visited nodes
        vis = set()
        st = []  # Stack to store nodes in their finishing order

        for i in range(V):
            # Perform DFS from unvisited nodes and store the nodes in a stack
            if i not in vis:
                self.dfs(vis, adj, st, i)

        # Step 2: Reverse the graph (transpose the adjacency list)
        adjR = [[] for _ in range(V)]  # Create an empty reversed graph

        for i in range(V):
            vis.remove(i)  # Clear the visited set for the second DFS pass
            for val in adj[i]:
                # In the transposed graph, reverse the direction of the edge `i -> val` to `val -> i`
                adjR[val].append(i)

        # Step 3: Process nodes in reverse finishing order to find SCCs
        scc = 0  # Counter for strongly connected components

        while st:
            # Get the next node based on the reverse order of finishing times
            tp_ele = st.pop()
            # If the node is unvisited in the reversed graph, start a new DFS from it
            if tp_ele not in vis:
                scc += 1  # Increment SCC count for each new DFS started
                # DFS on the reversed graph from this node to mark all nodes in this SCC
                self.dfs(vis, adjR, [], tp_ele)

        return scc  # Return the number of strongly connected components
