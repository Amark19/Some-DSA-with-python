# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []

        def preorder_traverse(node):
            if node:
                arr.append(node)
                preorder_traverse(node.left)
                preorder_traverse(node.right)

        preorder_traverse(root)
        for i in range(len(arr) - 1):
            arr[i].right = arr[i + 1]
            arr[i].left = None
