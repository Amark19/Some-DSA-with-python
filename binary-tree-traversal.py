ls = []
def inorder_traverse(root):
    if root is None:
        return
    inorder_traverse(root.left)
    ls.append(root.val)
    inorder_traverse(root.right)

def preorder_traverse(root):
    if root is None:
        return
    ls.append(root.val)
    inorder_traverse(root.left)
    inorder_traverse(root.right)

def postorder_traverse(root):
    if root is None:
        return
    ls.append(root.val)
    inorder_traverse(root.left)
    inorder_traverse(root.right)
inorder_traverse(root)
print("Inorder",ls)
ls = []
preorder_traverse(root)
print("preorder",ls)
ls = []
postorder_traverse(root)
print("postorder",ls)
