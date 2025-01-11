# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMid(node):
            curr, curr1 = node, node.next
            while curr and curr1 and curr1.next and curr1.next.next:  # fast traversal
                curr = curr.next
                if curr1.next:
                    curr1 = curr1.next.next
            return curr

        def mergeSort(node):
            if node and node.next is None:
                return node
            if node:
                left = node
                mid = getMid(left)
                right = mid.next
                mid.next = None
                left_s = mergeSort(left)
                right_s = mergeSort(right)
                return merge(left_s, right_s).next

        def merge(left, right):
            dummy_node = ListNode(-1)
            temp = dummy_node
            while left and right:
                if left.val > right.val:
                    temp.next = right
                    right = right.next
                else:
                    temp.next = left
                    left = left.next
                temp = temp.next
            temp.next = left or right
            return dummy_node

        return mergeSort(head)
