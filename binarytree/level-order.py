# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        if root is None: return []
        ans, q = [[root.val]], [root]
        while q:
            tmp = []
            for i in range(len(q)):
                node = q[0]
                if node and node.left:
                    q.append(node.left)
                    tmp.append(node.left.val)
                if node and node.right:
                    q.append(node.right)
                    tmp.append(node.right.val)
                del q[0]
            if tmp != []:
                ans.append(tmp)
        return ans
