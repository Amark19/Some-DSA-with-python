class Solution:
    def connect(self, root: 'Node') -> 'Node':
        arr = []

        def bfs(node, q):
            q_len = 0
            while q:
                node, layer = q[0]
                if node:
                    if q_len >= 1 and layer == q[1][1]:
                        node.next = q[1][0]
                    else:
                        node.next = None
                del q[0]
                q_len -= 1
                if node and node.left:
                    q.append((node.left, layer + 1))
                    q_len += 1
                if node and node.right:
                    q.append((node.right, layer + 1))
                    q_len += 1

        bfs(root, [(root, 0)])
        return root
