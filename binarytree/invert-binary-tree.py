class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # slight modifications in postorder
        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                # printing node
                left, right = None, None
                if node.left: left = node.left
                if node.right: right = node.right
                node.right = left
                node.left = right
                return node

        return postorder(root)
