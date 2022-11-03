# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr,count = head,0
        while curr is not None:
            curr,count = curr.next,count+1
        if count == n:return head.next
        temp,i = head,0
        while count - n > i:
            i,prev,temp = i+1,temp,temp.next
        prev.next = temp.next
        return head
      
   ##simplified
        curr = head
        count = 0
        while curr is not None:
            curr = curr.next
            count += 1
        if count == n:
            return head.next
        temp = head
        curr_i = 0
        while count - n > curr_i:
            curr_i+=1
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None
        return head   
