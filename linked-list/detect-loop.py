# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ls = []
        while head:
            if head in ls: return 1
            ls.append(head);
            head = head.next
        return 0

    # O(1) constant space time
#         prev,nex = head,head
#         while prev and nex and nex.next:
#             prev = prev.next#2 0 -4 
#             nex = nex.next.next#0 -4 2
#             if prev is nex:
#                 print(prev,nex)
#                 return 1
#         return 0
