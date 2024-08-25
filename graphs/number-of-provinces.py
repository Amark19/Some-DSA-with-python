class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        visted_arr = set()

        def traverse(node, visted_arr):
            visted_arr.add(node)
            for i in range(m):
                if i not in visted_arr and isConnected[node][i] == 1:
                    traverse(i, visted_arr)

        cnt = 0
        for node in range(m):
            if node not in visted_arr:
                traverse(node, visted_arr)
                cnt += 1
        return cnt