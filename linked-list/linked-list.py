class node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class linkedlist:
    def __init__(self):
        self.headval = None

    def printlist(self):
        printval = self.headval
        while printval != None:
            print(printval.val)
            printval = printval.next

    def insertAtBegin(self):
        new_node = node(0)
        new_node.next = self.headval
        self.headval = new_node

    def insertAtEnd(self):
        new_node = node(4)
        if self.headval is None:
            self.headval = new_node
            return
        val = self.headval
        while val.next != None:
            val = val.next
        val.next = new_node

    def insertAnyWhere(self, pos, newNode):
        count = 1
        val = self.headval
        while count < pos:
            val = val.next
            count += 1
        newNode.next = val.next
        val.next = newNode

    def deleteAtBegin(self):
        self.headval = self.headval.next

    def deleteAnyWhere(self, pos):
        temp = self.headval
        count = 0
        while count < pos:
            count += 1
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None


n1 = node(1)
n2 = node(2)
n3 = node(3)

n1.next = n2
n2.next = n3

list1 = linkedlist()
##insertion
print("##After Insertion###")
list1.insertAtBegin()
list1.insertAtEnd()
list1.insertAnyWhere(2, node(5))
list1.printlist()
print()
print("##After Deletion###")
list1.deleteAtBegin()
list1.deleteAnyWhere(3)
list1.printlist()
