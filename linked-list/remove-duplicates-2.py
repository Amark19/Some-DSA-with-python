class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                duplicate_val = head.val
                while head and head.val == duplicate_val:
                    head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next

        return dummy.next
