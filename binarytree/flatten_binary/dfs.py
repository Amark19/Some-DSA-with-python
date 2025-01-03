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

        def dfs(node, count):
            left, right = None, None
            last_node_left, last_node_right = node, node
            left_count, right_count = 0, 0
            if node:
                if node.left:
                    left = node.left
                    last_node = left
                if node.right:
                    right = node.right
                if left:
                    node.right = left
                    node.left = None
                    last_node_left, left_count = dfs(left, count + 1)
                if right:
                    if last_node_left:
                        last_node_left.right = right
                        last_node_left.left = None
                    last_node_right, right_count = dfs(right, count + 1)
            if left_count > right_count:
                return (last_node_left, count)
            else:
                return (last_node_right, count)

        dfs(root, 0)
