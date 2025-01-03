class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map to store the index of each value in the inorder traversal
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0  # Pointer to track the current root in preorder

        def helper(left: int, right: int) -> Optional[TreeNode]:
            # Base case: if there are no elements to construct the subtree
            if left > right:
                return None

            # Select the current root from preorder traversal
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Build left and right subtrees using the inorder index map
            root.left = helper(left, inorder_map[root_val] - 1)
            root.right = helper(inorder_map[root_val] + 1, right)

            return root

        # Start building the tree from the entire inorder range
        return helper(0, len(inorder) - 1)
