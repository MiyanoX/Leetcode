# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head.next is None:
            return head
        
        # two pointer
        slow = head
        fast = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        return slow