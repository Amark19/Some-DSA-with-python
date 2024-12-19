# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i, j = 0, 0
        curr1, curr2 = headA, headB
        while curr1 or curr2:
            if curr1 is not None: curr1 = curr1.next;i += 1
            if curr2 is not None: curr2 = curr2.next; j += 1
        curr1, curr2 = headA, headB
        while i > j:
            curr1 = curr1.next
            j += 1
        while j > i:
            curr2 = curr2.next
            i += 1
        while curr1 or curr2:
            if curr1 == curr2: return curr1
            curr1 = curr1.next
            curr2 = curr2.next
