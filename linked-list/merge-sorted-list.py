# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Merge sort approach
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr1, curr2, curr3 = list1, list2, ListNode()
        demo = curr3
        while curr1 != None and curr2 != None:
            # if curr1 != None or curr2 != None:continue
            if curr1.val < curr2.val:
                curr3.next = ListNode(curr1.val)
                curr1 = curr1.next

            else:
                curr3.next = ListNode(curr2.val)
                curr2 = curr2.next
            curr3 = curr3.next
        while curr1 != None:
            curr3.next = ListNode(curr1.val)
            curr1 = curr1.next
            curr3 = curr3.next
        while curr2 != None:
            curr3.next = ListNode(curr2.val)
            curr2 = curr2.next
            curr3 = curr3.next
        return demo.next
