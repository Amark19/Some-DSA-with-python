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


"""
strongly connected components are the components in a graph where every node is reachable from every other node in the component.
if u->v is reachable then v->u should also be reachable

IN KOSARAJU'S ALGORITHM:
Consider a graph,
0 <- 2 -> 3 -> 4 -> 7
| /            | \  | 
1              5 -> 6

0, 1, 2 are strongly connected components
3 is a strongly connected component
4, 5, 6 are strongly connected components
7 is a strongly connected component

The algorithm works as follows:
1. Perform a DFS traversal on the original graph and keep track of the finishing order of nodes.
2. Reverse the edges of the graph to create the transposed graph.
3. Process nodes in the reverse order of finishing time to find strongly connected components.(dfs)

Why This Order Matters for SCCs
In Kosaraju’s algorithm, the order of nodes based on their finishing times has a specific purpose:

Source Nodes in SCCs: In a directed graph, SCCs are like "closed loops" where every node in the SCC can reach every other node in that SCC. However, the SCC itself can be thought of as having a "source" node when looking at connections between different SCCs.

Processing in Reverse Order: When we reverse the graph, starting from nodes in the reverse finishing order ensures that we handle each SCC separately without accidentally merging nodes from different SCCs. In essence, it helps isolate each SCC.
"""