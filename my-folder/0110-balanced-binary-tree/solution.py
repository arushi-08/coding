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
        
        left = self.isBalanced(root.left)
        right = self.isBalanced(root.right)
        leftht = self.helper(root.left)
        rightht = self.helper(root.right)
        
        return left and right and abs(leftht - rightht) <= 1
        
    def helper(self, root):
        if not root:
            return 0
        
        left = self.helper(root.left) + 1
        right = self.helper(root.right) + 1
        return max(left, right)
