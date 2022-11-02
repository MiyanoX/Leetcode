class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return root and (self.isEqual(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
		# return false if root is None
		# then return comparison of root and subRoot
		# along with recursive in right and left child
    
    def isEqual(self, t1, t2):
            if t1 and t2 and t1.val == t2.val:
                return self.isEqual(t1.left, t2.left) and self.isEqual(t1.right, t2.right)
            else:
                return t1 == t2
			# recursive while two value is equal
			# return True if both are None
			# else return Flase