# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root)
    
    def helper(self, root):
        if not root:
            return True
        lans = self.helper(root.left)
        rans = self.helper(root.right)
        maxdepth = self.maxDepth(root)
        mindepth = self.minDepth(root)
        if maxdepth - mindepth > 1:
            return False
        return lans and rans and True
    
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def minDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return min(left, right) + 1

