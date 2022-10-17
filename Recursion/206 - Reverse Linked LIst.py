class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        while head.next:
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        head.next = prev
        return head