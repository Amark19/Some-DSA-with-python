class Node:
    def __init__(self, node_val):
        self.val = node_val
        self.left = None
        self.right = None
        self.height = 1


class Avl:
    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rightRotate(self, node):
        left = node.left
        left_right = left.right

        left.right = node
        node.left = left_right

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left.height = 1 + max(self.height(left.left), self.height(left.right))
        return left

    def leftRotate(self, node):
        right = node.right
        right_left = right.left

        right.left = node
        node.right = right_left

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right.height = 1 + max(self.height(right.left), self.height(right.right))
        return right

    def insert(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.val:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)
        if balance > 1 and key < node.left.val:
            return self.rightRotate(node)
        if balance < -1 and key > node.right.val:
            return self.leftRotate(node)
        if balance > 1 and key > node.left.val:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and key < node.right.val:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node


def preOrder(node):
    if not node:
        return
    print(node.val, end=" ")
    preOrder(node.left)
    preOrder(node.right)


avl = Avl()
root = None
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = avl.insert(root, key)
preOrder(root)