# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start, end = head, head

        for _ in range(n):
            end = end.next
            
        if not end:
            return head.next

        while end.next:
            start, end = start.next, end.next
        
        start.next = start.next.next
        
        return head