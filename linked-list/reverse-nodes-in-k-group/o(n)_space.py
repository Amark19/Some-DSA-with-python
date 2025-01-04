# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1: return head

        def perform_reversal(node):
            prev = None
            curr = node
            nex = None
            while curr:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            node = prev
            return node

        curr = head
        prev = head
        count = 0
        arr = []
        while curr:
            count += 1
            if count % k == 0:
                nex = curr.next
                curr.next = None
                # lets a perform reversal
                prev = perform_reversal(prev)
                arr.append(prev)
                curr = nex
                prev = curr
                count += 1
            if curr: curr = curr.next
        tmp = arr[0]
        tmp_1 = tmp
        for i in range(len(arr) - 1):
            tmp_1 = arr[i]
            while tmp_1.next:
                tmp_1 = tmp_1.next
            tmp_1.next = arr[i + 1]
        while tmp_1.next:
            tmp_1 = tmp_1.next
        tmp_1.next = prev
        return tmp
