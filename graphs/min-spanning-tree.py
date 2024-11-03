# User function Template for python3
from typing import List
import heapq


class Solution:

    # Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        # code here
        su = 0
        vis = set()
        mst = (())
        p_que = [(0, 0, -1)]  # (wt,node,parent)

        while p_que:
            wt, node, parent = heapq.heappop(p_que)
            if node in vis: continue
            vis.add(node)
            su += wt
            for adj_node in adj[node]:
                dest, a_wt = adj_node
                if dest not in vis:
                    heapq.heappush(p_que, (a_wt, dest, node))
        return su