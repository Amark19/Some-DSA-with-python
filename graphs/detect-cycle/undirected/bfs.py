from typing import List

class Solution:
    def checkCycle(self, adj, visited_arr, src):
        que = []

        visited_arr.add(src)
        que.append((src, -1))  # node, source
        while len(que) > 0:
            node, source = que[0]
            for val in adj[node]:
                if val not in visited_arr:
                    que.append((val, que[0][0]))
                    visited_arr.add(val)
                elif val != source:
                    return True

            del que[0]
        # print()
        return False

    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        # Code here
        visited_arr = set()
        for val in range(V):
            if val not in visited_arr:
                if self.checkCycle(adj, visited_arr, val):
                    return True
        return False


# {
# Driver Code Starts

if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends