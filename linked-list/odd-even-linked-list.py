# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:return head
        curr,i = head,1
        node1,node2 = ListNode(),ListNode()
        temp1,temp2 = node1,node2
        while curr:
            if i%2 != 0:temp1.next = ListNode(curr.val);temp1 = temp1.next
            else:temp2.next = ListNode(curr.val);temp2 = temp2.next
            curr = curr.next;i += 1
        temp1 = node1.next
        while temp1.next:temp1 = temp1.next
        temp1.next = node2.next
        return node1.next