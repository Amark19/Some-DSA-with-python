# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr != None:
            if curr.next != None and curr.val == curr.next.val:
                temp = curr.next
                curr.next = temp.next
                temp = None
            else:
                curr = curr.next
        return head
