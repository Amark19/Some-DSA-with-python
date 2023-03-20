# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        if root == None:return []
        def bfs(q,ls):
            while q:
                for i in range(len(q)):
                    node = q[0]
                    if node and node.left:q.append(node.left)
                    if node and node.right:q.append(node.right)
                    del q[0]
                if q:ls.append(q[-1].val)
            return ls
        
        return bfs([root],[root.val])
