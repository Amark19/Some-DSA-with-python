# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2,carry = l1,l2,0
        dum = ListNode()
        curr = dum
        while curr1 is not None or curr2 is not None or carry is not 0:
            x,y = 0,0
            if curr1 is not None:x = curr1.val;curr1 = curr1.next
            if curr2 is not None:y = curr2.val;curr2 = curr2.next
            su = x+y+carry
            carry = su // 10
            curr.next = ListNode(su % 10)
            curr = curr.next
        return dum.next
