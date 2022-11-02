class node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def max_depth(root):
    if root is None:
        return 0
    left_child = max_depth(root.left)
    right_child = max_depth(root.right)
    return max(left_child,right_child) + 1

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
print(max_depth(root))
