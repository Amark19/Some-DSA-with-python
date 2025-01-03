class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        current = root
        while current:
            if current.left:
                # Find the rightmost node in the left subtree
                predecessor = current.left
                while predecessor.right:
                    predecessor = predecessor.right

                # Connect the right subtree to the rightmost node
                predecessor.right = current.right

                # Make the left subtree the right subtree
                current.right = current.left
                current.left = None

            # Move to the next node in preorder
            current = current.right
