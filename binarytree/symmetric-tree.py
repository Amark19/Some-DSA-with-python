# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ls_l,ls_r = [],[]
        def traverse_left(root):
            if root is not None:
                ls_l.append(root.val)
                traverse_left(root.left)
                traverse_left(root.right)
            else:
                ls_l.append(None)
                return
        def traverse_right(root):
            if root is not None:
                ls_r.append(root.val)
                traverse_right(root.right)
                traverse_right(root.left)
            else:
                ls_r.append(None)
                return
        
        traverse_left(root.left);traverse_right(root.right)
        if ls_l == ls_r:return 1
        else:return 0
        print(ls_l,ls_r)
