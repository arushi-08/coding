# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        if not subRoot: return True
        curr = self.helper(root, subRoot)
        if curr:
            return True
        left = self.isSubtree(root.left, subRoot)
        if left:
            return True
        right = self.isSubtree(root.right, subRoot)
        return right
    
    def helper(self, root, subroot):
        if not root and not subroot:
            return True
        if not root:
            return False
        if not subroot:
            return False

        if root.val == subroot.val:
            left = self.helper(root.left, subroot.left)
            right = self.helper(root.right, subroot.right)
            if left and right:
                return True
