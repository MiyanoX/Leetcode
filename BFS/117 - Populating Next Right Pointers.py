class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:                        # return root is None
            return root
        
        queue = [root, None]                # set first level of Node
        while queue != [None]:              # while until no item left
            cur = queue.pop(0)
            if not cur:
                queue.append(None)
                continue
            cur.next = queue[0]
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return root