# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]##whole list in arr
        while arr[-1].next:#till this get None
            arr.append(arr[-1].next)#appending next of last node in array i.e 1->next[2,3,4,5],2->next[3,4,5] & soo one
        return arr[len(arr) // 2]#then return the mid of arr which is [1->next,2->next,3->next,4->next]# mid would be 3-> next that is 3,4,5
