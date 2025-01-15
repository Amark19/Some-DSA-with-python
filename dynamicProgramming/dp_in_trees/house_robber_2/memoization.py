class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}

        def dfs(node):
            if not node:
                return 0
            if node in dp:
                return dp[node]
            # Include the current node (skip immediate children)
            include = node.val
            if node.left:
                include += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                include += dfs(node.right.left) + dfs(node.right.right)

            # Exclude the current node (take the max of children)
            exclude = dfs(node.left) + dfs(node.right)
            dp[node] = max(include, exclude)
            return dp[node]

        return dfs(root)
