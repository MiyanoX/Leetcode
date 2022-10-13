"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = [None, root]
        while queue:
            cur = queue.pop()
            if not cur:
                continue
            cur.next = queue[-1]           
            queue = [cur.right, cur.left] + queue
            if not cur.next:
                queue.insert(0, None)
        return root
    
    
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = root
        while root and root.left:
            next = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next
            root = next
        return head