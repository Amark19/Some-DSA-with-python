# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def isPalindrome(head) -> bool:
    curr = head
    ls = []
    while curr is not None:
        ls.append(curr.val)
        curr = curr.next
    if ls == ls[::-1]:
        return True
    return False

head = ListNode(1)
#ad elements
n1 = ListNode(2)
n2 = ListNode(2)
n3 = ListNode(1)
head.next = n1
n1.next = n2
n2.next = n3
print(isPalindrome(head))