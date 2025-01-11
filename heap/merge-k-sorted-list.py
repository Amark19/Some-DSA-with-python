# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tmp = dummy
        heap = []
        # push smallest of each into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            val, index, node = heapq.heappop(heap)
            tmp.next = node
            tmp = tmp.next
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
        return dummy.next
