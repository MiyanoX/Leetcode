# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
		# edge case
        if depth == 1:
            new_root = TreeNode(val, left=root)
            return new_root
        
		# record the current depth
        depth_count = 1
		# record all nodes in current depth
        node_list = [root]
        
		# judge if still nodes in current depth and current_depth is lower than given depth
        while node_list and depth_count < depth:
		
			# if current depth is equal to depth - 1, add left and right nodes with val to all nodes in this depth
            if depth_count == depth - 1:
                for node in node_list:
                    left, right = node.left, node.right
                    node.left = TreeNode(val, left=left)
                    node.right = TreeNode(val, right=right)
                return root
            else:
			
				# go on to next depth
                new_list = []
                for node in node_list:
                    if node.left:
                        new_list.append(node.left)
                    if node.right:
                        new_list.append(node.right)
                node_list = new_list
                depth_count += 1
        return root