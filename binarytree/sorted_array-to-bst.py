nums = [] #sorted list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def arrangbst(ls):
    if len(ls) == 0:
        return None
    mid = len(ls)//2
    root = TreeNode(ls[mid])
    root.left = arrangbst(ls[:mid])
    root.right = arrangbst(ls[mid+1:])
    return root
root = arrangbst(nums)
return root
