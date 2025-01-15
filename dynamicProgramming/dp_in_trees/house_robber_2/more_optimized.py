def rob(self, root: TreeNode) -> int:
    def dfs(node):
        if not node:
            return (0, 0)

        # Recursively call for left and right subtrees
        left = dfs(node.left)
        right = dfs(node.right)

        # If we rob this node, we cannot rob its children
        rob_current = node.val + left[1] + right[1]

        # If we don't rob this node, we can rob the children
        not_rob_current = max(left) + max(right)

        # Return two values:
        # 1. The maximum amount we can rob if we rob this node
        # 2. The maximum amount we can rob if we don't rob this node
        return (rob_current, not_rob_current)

    # Start the recursion from the root
    return max(dfs(root))