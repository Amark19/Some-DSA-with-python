class node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.headval = None
    def printlist(self):
        printval = self.headval
        while printval!=None:
            print(printval.val)
            printval = printval.next
    def insertAtBegin(self):
        new_node = node(0)
        new_node.next = self.headval
        self.headval = new_node

list1 = linkedlist()
list1.headval = node(1)
n2 = node(2)
n3 = node(3)

list1.headval.next = n2
n2.next = n3
list1.insertAtBegin()
list1.printlist()
