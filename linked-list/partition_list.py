# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        curr = ListNode(-1, head)
        left, right = curr, curr.next
        dummy = ListNode(0)
        dummy_1 = dummy

        while left and right:
            if right.val < x:
                left.next = right
                left = left.next
            else:
                dummy_1.next = right
                dummy_1 = dummy_1.next
            right = right.next
        dummy_1.next = None
        left.next = None
        left.next = dummy.next
        return curr.next
