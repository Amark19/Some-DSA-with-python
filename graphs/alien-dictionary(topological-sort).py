class Solution:
    def findOrder(self, dict: List[str], n: int, V: int) -> str:
        # Your implementation here
        def convertToIn(char):
            return (ord(char) - 96) - 1

        def convertToChar(intg):
            return
            # Create adjacency list

        adj = [[] for _ in range(V)]
        for i in range(n - 1):
            s1 = dict[i]
            s2 = dict[i + 1]
            rg = min(len(s1), len(s2))
            for j in range(rg):
                if s1[j] != s2[j]:
                    adj[convertToIn(s1[j])].append(convertToIn(s2[j]))
                    break
        indegree = V * [0]
        for v in range(V):
            for node in adj[v]:
                indegree[node] += 1
        q = []
        top = []
        for v in range(V):
            if indegree[v] == 0: q.append(v)
        while q:
            node = q[0]
            del q[0]
            top.append(node)
            for nd in adj[node]:
                indegree[nd] -= 1
                if indegree[nd] == 0:
                    q.append(nd)
        return ''.join(chr(i + ord('a')) for i in top)