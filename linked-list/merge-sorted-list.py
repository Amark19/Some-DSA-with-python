# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2,curr3 = list1,list2,ListNode()
        demo = curr3
        while curr1 != None or curr2 != None :
            if curr1 != None and curr2 == None:
                curr3.next = ListNode(curr1.val)
                curr3 = curr3.next
                curr1 = curr1.next
            elif curr2 != None and curr1 == None:
                curr3.next = ListNode(curr2.val)
                curr3 = curr3.next
                curr2 = curr2.next
            else:
                if curr1.val >= curr2.val :
                    curr3.next = ListNode(curr2.val)
                    curr3 = curr3.next
                    curr2 = curr2.next
                else:
                    curr3.next = ListNode(curr1.val)
                    curr3 = curr3.next
                    curr1 = curr1.next
        return demo.next
        
