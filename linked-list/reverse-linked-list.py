class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def reverse(self):
        prev = None
        nex = None
        cur = self.head
        # can be easily visualize by three pointers
        #0th iteration
        #none 0    1       2
        #prev curr next
        #1st iteration
        #0    1       2
        #prev curr next
        while cur!=None:
            nex = cur.next 
            cur.next = prev 
            prev = cur
            cur = nex
        self.head = prev
    def printlist(self):
        printval = self.head
        while printval!=None:
            print(printval.data)
            printval = printval.next
ls = linkedlist()
ls.head = node(0)
n1 = node(1)
n2 = node(2)
ls.head.next = n1
n1.next = n2
ls.printlist()
ls.reverse()
ls.printlist()

1->2->3->4->5

1.next = 1

2->
