class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevHead = ListNode(next=head)                      # create node as a previous point for delete next nodes 
        prev = prevHead                     
        while prev.next and prev.next.next:                 # check if next node two nodes are exist
            if prev.next.val == prev.next.next.val:         # check if next two nodes are equal
                tmp = prev.next.next
                while tmp and tmp.val == prev.next.val:     # find the next node of last duplicate node
                    tmp = tmp.next
                prev.next = tmp                             # set next node of previous node
            else:
                prev = prev.next                            # if node is not duplicate, then go on

        return prevHead.next
            