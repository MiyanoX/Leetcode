# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(next=head)
        head_prev = start
        end = head
        
        while n > 1:
            end = end.next
            n -= 1
            
        while end.next != None:
            start, end = start.next, end.next
        
        start.next = start.next.next
        
        return head_prev.next