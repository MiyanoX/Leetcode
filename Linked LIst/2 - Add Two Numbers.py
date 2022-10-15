# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        addition = 0
        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val + addition
                l1, l2 = l1.next, l2.next
            elif l1:
                value = l1.val + addition
                l1 = l1.next
            elif l2:
                value = l2.val + addition
                l2 = l2.next            
                
            current.next = ListNode(value % 10)
            addition = value // 10
            current = current.next
        
        if addition:
            current.next = ListNode(addition)
            
        return head.next
            