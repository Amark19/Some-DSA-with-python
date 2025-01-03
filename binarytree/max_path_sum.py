# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        arr = []

        def dfs(node):
            if node:
                val = node.val
                mx_left = dfs(node.left)
                mx_right = dfs(node.right)
                arr.append(max(mx_left + mx_right + node.val, val, mx_left, mx_right))
                return max(mx_left + val, mx_right + val, val)
            else:
                return float("-inf")

        mx = dfs(root)
        return max(max(arr), mx)
