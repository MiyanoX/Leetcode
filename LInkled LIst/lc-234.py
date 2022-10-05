# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # single node case
        if head.next is None:
            return True
        
        # two pointer to find the middle point of linked list
        first_pointer = head
        second_pointer = head.next
        
        while second_pointer and second_pointer.next:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next
        
        # reverse the second half of linked list
        prev_node = None
        current_node = first_pointer.next
        
        while current_node != None:
            temp = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp
        
        # judge if is palindrome from head and last node
        last = prev_node
        
        while last != None:
            if head.val != last.val:
                return False
            head = head.next
            last = last.next
            
        return True
            
            
        
        