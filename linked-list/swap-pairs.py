# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify edge cases
        dummy = ListNode(0, head)
        prev = dummy

        # Traverse the list in pairs
        while prev.next and prev.next.next:
            # Identify the pair
            first = prev.next
            second = first.next

            # Swap the pair
            first.next = second.next
            second.next = first
            prev.next = second

            # Move to the next pair
            prev = first

        return dummy.next
