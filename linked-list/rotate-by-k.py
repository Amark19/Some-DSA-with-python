# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:return None
        length,curr = 0,head
        while curr:curr = curr.next;length += 1
        t = head
        for i in range(k%(length)):
            curr = temp = t
            while curr:
                if curr.next.next is None:
                    t = curr.next
                    curr.next = None
                    break
                curr = curr.next
            t.next = temp
        return t
