class node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def inorder_traverse(self,root):
        if root is None:
            return
        self.inorder_traverse(root.left)
        ls.append(root.val)
        self.inorder_traverse(root.right)

    def preorder_traverse(self,root):
        if root is None:
            return
        ls.append(root.val)
        self.inorder_traverse(root.left)
        self.inorder_traverse(root.right)

    def postorder_traverse(self,root):
        if root is None:
            return
        self.inorder_traverse(root.left)
        self.inorder_traverse(root.right)
        ls.append(root.val)
root = node(1)
n2 = node(2)
n3 = node(3)
n4 = node(4)
root.left = n2
root.right = n3
n3.left = n4

T = Tree()
T.root = root

ls = []
T.inorder_traverse(root)
print("Inorder",ls)
ls = []
T.preorder_traverse(root)
print("preorder",ls)
ls = []
T.postorder_traverse(root)
print("postorder",ls)
